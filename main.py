import heapq
import random
import argparse
import math

# Event types
EVENT_GENERATE_PDU_SESSION = 1
EVENT_TERMINATE_PDU_SESSION = 2
EVENT_SCALE_OUT = 3
EVENT_SCALE_IN = 4


class Event:
    """
    Represents an event in the simulation.
    """

    def __init__(self, event_type, time):
        """
        Initialize an event with its type and time.

        :param event_type: Type of the event.
        :param time: Time at which the event occurs.
        """
        self.event_type = event_type
        self.time = time

    def __lt__(self, other):
        """
        Less than comparison for events based on time.

        :param other: Another event object.
        :return: True if this event occurs earlier than the other event.
        """
        return self.time < other.time


class PDUSession:
    """
    Represents a PDU session in the simulation.
    """

    def __init__(self, session_id, start_time, duration):
        """
        Initialize a PDU session with its ID, start time, and duration.

        :param session_id: ID of the session.
        :param start_time: Start time of the session.
        :param duration: Duration of the session.
        """
        self.session_id = session_id
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration


class UPF:
    """
    Represents a UPF (User Plane Function) in the simulation.
    """

    def __init__(self, upf_id):
        """
        Initialize a UPF with its ID.

        :param upf_id: ID of the UPF.
        """
        self.upf_id = upf_id
        self.sessions = []

    def add_session(self, session):
        """
        Add a session to the UPF.

        :param session: Session object to be added.
        """
        self.sessions.append(session)

    def remove_session(self, session):
        """
        Remove a session from the UPF.

        :param session: Session object to be removed.
        """
        self.sessions.remove(session)


class Scheduler:
    """
    Implements the event-based scheduler simulation.
    """

    def __init__(self, max_upf_instances, min_upf_instances, max_sessions_per_upf, scale_out_threshold,
                 scale_in_threshold, simulation_time, output_file):
        """
        Initialize the scheduler with simulation parameters.

        :param max_upf_instances: Maximum number of UPF instances (L).
        :param min_upf_instances: Minimum number of UPF instances (M).
        :param max_sessions_per_upf: Maximum number of sessions per UPF (C).
        :param scale_out_threshold: Scale-out threshold (T1).
        :param scale_in_threshold: Scale-in threshold (T2).
        :param simulation_time: Total simulation time.
        :param output_file: File to write simulation outputs.
        """
        self.event_queue = []
        self.upfs = []
        self.max_upf_instances = max_upf_instances
        self.min_upf_instances = min_upf_instances
        self.max_sessions_per_upf = max_sessions_per_upf
        self.scale_out_threshold = scale_out_threshold
        self.scale_in_threshold = scale_in_threshold
        self.num_upf_instances = 0
        self.next_upf_id = 0
        self.session_counter = 0
        self.current_time = 0
        self.simulation_time = simulation_time
        self.output_file = output_file

    def _log(self, message):
        """
        Log a message to the output file.

        :param message: Message to be logged.
        """
        with open(self.output_file, 'a') as f:
            f.write(message + '\n')

    def generate_pdu_session(self):
        """
        Generate a new PDU session event.
        """
        message = f"Time: {self.current_time}, UE generates PDU session"
        self._log(message)
        session_id = self.session_counter
        self.session_counter += 1
        duration = math.ceil(-math.log(random.uniform(0, 1)) * 5)  # Exponential distribution between 1 and 5
        session = PDUSession(session_id, self.current_time, duration)

        # Find an available UPF
        available_upf = next((upf for upf in self.upfs if len(upf.sessions) < self.max_sessions_per_upf), None)

        # If no available UPF, scale out if possible
        if not available_upf:
            if self.num_upf_instances < self.max_upf_instances:
                self.scale_out()
                available_upf = self.upfs[-1]
            else:
                message = f"Time: {self.current_time}, Cannot scale out due to maximum UPF instances reached"
                self._log(message)
                message = (f"Time: {self.current_time}, Cannot assign PDU session to UPF because of resource "
                           f"constraints, terminating PDU session")
                self._log(message)
                self.terminate_pdu_session(session)

        if available_upf:
            if len(available_upf.sessions) >= self.max_sessions_per_upf - self.scale_out_threshold:
                self.scale_out()
                available_upf = self.upfs[-1]

            message = f"Time: {self.current_time}, UE sends PDU session {session_id} request to Compute Node"
            self._log(message)
            available_upf.add_session(session)
            end_event = Event(EVENT_TERMINATE_PDU_SESSION, self.current_time + duration)
            heapq.heappush(self.event_queue, end_event)

            message = (f"Time: {self.current_time}, Compute Node allocates UPF {available_upf.upf_id} for PDU session "
                       f"{session_id}")
            self._log(message)
            message = f"Time: {self.current_time}, PDU Session {session_id} started on UPF {available_upf.upf_id}"
            self._log(message)

    def terminate_pdu_session(self, session):
        """
        Terminate a PDU session.

        :param session: Session to be terminated.
        """
        upf = next((upf for upf in self.upfs if session in upf.sessions), None)
        message = f"Time: {self.current_time}, PDU Session {session.session_id} terminated on UPF {upf.upf_id}"
        self._log(message)
        if upf:
            upf.remove_session(session)
            if self.num_upf_instances > self.min_upf_instances and len(
                    upf.sessions) == self.max_sessions_per_upf - self.scale_in_threshold:
                self.scale_in(upf)

    def scale_out(self):
        """
        Scale out by launching a new UPF instance.
        """
        if self.num_upf_instances < self.max_upf_instances:
            new_upf_id = self.next_upf_id
            self.next_upf_id += 1
            new_upf = UPF(new_upf_id)
            self.upfs.append(new_upf)
            self.num_upf_instances += 1
            message = f"Time: {self.current_time}, Compute Node launches UPF {new_upf_id}"
            self._log(message)

    def scale_in(self, upf):
        """
        Scale in by terminating a UPF instance.

        :param upf: UPF instance to be terminated.
        """
        if upf.upf_id >= self.min_upf_instances:
            self.upfs.remove(upf)
            self.num_upf_instances -= 1
            message = f"Time: {self.current_time}, Compute Node terminates UPF {upf.upf_id}"
            self._log(message)

    def run(self):
        """
        Run the simulation.
        """
        # Schedule the initial PDU session generation
        generation_event = Event(EVENT_GENERATE_PDU_SESSION, 0)
        heapq.heappush(self.event_queue, generation_event)

        while self.current_time < self.simulation_time or self.event_queue:
            if not self.event_queue:
                break

            event = heapq.heappop(self.event_queue)
            self.current_time = event.time

            if event.event_type == EVENT_GENERATE_PDU_SESSION:
                self.generate_pdu_session()

                # Schedule the next PDU session generation
                next_generation_time = self.current_time + random.randint(1, 10)  # Random interval between 1 and 10
                # time units
                if next_generation_time <= self.simulation_time:
                    generation_event = Event(EVENT_GENERATE_PDU_SESSION, next_generation_time)
                    heapq.heappush(self.event_queue, generation_event)

            elif event.event_type == EVENT_TERMINATE_PDU_SESSION:
                session = next(
                    (session for upf in self.upfs for session in upf.sessions if session.end_time == self.current_time),
                    None)
                if session:
                    self.terminate_pdu_session(session)

        # Terminate any remaining UPFs
        for upf in self.upfs:
            message = f"Time: {self.current_time}, Compute Node terminates UPF {upf.upf_id}"
            self._log(message)

        self._log(f"Simulation completed. Total PDU sessions processed: {self.session_counter}. "
                  f"Total UPFs deployed: {self.next_upf_id}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Event-based scheduler simulation")
    parser.add_argument("--max-upf-instances", type=int, default=4, help="Maximum number of UPF instances (L)")
    parser.add_argument("--min-upf-instances", type=int, default=1, help="Minimum number of UPF instances (M)")
    parser.add_argument("--max-sessions-per-upf", type=int, default=3, help="Maximum number of sessions per UPF (C)")
    parser.add_argument("--scale-out-threshold", type=int, default=2, help="Scale-out threshold (T1)")
    parser.add_argument("--scale-in-threshold", type=int, default=3, help="Scale-in threshold (T2)")
    parser.add_argument("--simulation-time", type=int, default=10000, help="Simulation time")
    parser.add_argument("--output-file", type=str, default="simulation.log", help="File to write simulation outputs")

    args = parser.parse_args()

    scheduler = Scheduler(args.max_upf_instances, args.min_upf_instances, args.max_sessions_per_upf,
                          args.scale_out_threshold, args.scale_in_threshold, args.simulation_time, args.output_file)
    scheduler.run()
