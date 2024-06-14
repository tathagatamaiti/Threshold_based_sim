import csv
import heapq
import random
import argparse
import numpy as np

# Event types
EVENT_GENERATE_PDU_SESSION = 1
EVENT_TERMINATE_PDU_SESSION = 2


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

    def __init__(self, upf_case, max_upf_instances, min_upf_instances, max_sessions_per_upf, scale_out_threshold,
                 scale_in_threshold, simulation_time, arrival_rate, mu, migration_case, output_file):
        """
        Initialize the scheduler with simulation parameters.

        :param upf_case: Case for UPF sorting.
        :param max_upf_instances: Maximum number of UPF instances (L).
        :param min_upf_instances: Minimum number of UPF instances (M).
        :param max_sessions_per_upf: Maximum number of sessions per UPF (C).
        :param scale_out_threshold: Scale-out threshold (T1).
        :param scale_in_threshold: Scale-in threshold (T2).
        :param simulation_time: Total simulation time.
        :param arrival_rate: Rate of session arrival (λ).
        :param mu: Session duration parameter (µ).
        :param migration_case: Case for session migration.
        :param output_file: File to write simulation outputs.
        """
        self.event_queue = []
        self.upfs = []
        self.upf_case = upf_case
        self.max_upf_instances = max_upf_instances
        self.min_upf_instances = min_upf_instances
        self.max_sessions_per_upf = max_sessions_per_upf
        self.scale_out_threshold = scale_out_threshold
        self.scale_in_threshold = scale_in_threshold
        self.arrival_rate = arrival_rate
        self.mu = mu
        self.migration_case = migration_case
        self.num_upf_instances = 0
        self.next_upf_id = 0
        self.session_counter = 0
        self.current_time = 0
        self.simulation_time = simulation_time
        self.active_sessions = 0  # I: number of sessions being served
        self.free_slots = 0  # U: number of free slots in the system
        self.output_file = output_file

    def _log(self, message):
        """
        Log a message to the output file.

        :param message: Message to be logged.
        """
        with open(self.output_file, 'a') as f:
            f.write(message + '\n')

    def update_free_slots(self):
        """
        Update the number of free slots in the system.
        """
        self.free_slots = sum(self.max_sessions_per_upf - len(upf.sessions) for upf in self.upfs)

    def get_upf_with_lowest_sessions(self):
        """
        Get the UPF with the lowest number of sessions.
        If multiple UPFs have the same lowest number of sessions, randomly select one.
        """
        upfs_sorted = sorted(self.upfs, key=lambda upf: len(upf.sessions))
        lowest_sessions_upfs = [upf for upf in upfs_sorted if len(upf.sessions) == len(upfs_sorted[0].sessions)]
        return random.choice(lowest_sessions_upfs)

    def generate_pdu_session(self):
        """
        Generate a new PDU session event.
        """
        message = f"Time: {np.ceil(self.current_time)}, UE generates PDU session"
        self._log(message)
        session_id = self.session_counter
        self.session_counter += 1
        duration = (np.random.exponential(1 / self.mu) * 1000)
        session = PDUSession(session_id, np.ceil(self.current_time), duration)

        # Find an available UPF
        if self.upf_case == 1:
            available_upf = next((upf for upf in self.upfs if len(upf.sessions) < self.max_sessions_per_upf), None)
        elif self.upf_case == 2:
            available_upf = self.get_upf_with_lowest_sessions() if self.upfs else None
        else:
            message = f"Time: {np.ceil(self.current_time)}, No UPF available"
            self._log(message)

        # If no available UPF, scale out if possible
        if not available_upf:
            if self.num_upf_instances < self.max_upf_instances:
                self.scale_out()
                available_upf = self.upfs[-1]
            else:
                message = f"Time: {np.ceil(self.current_time)}, Cannot scale out due to maximum UPF instances reached"
                self._log(message)
                message = (f"Time: {np.ceil(self.current_time)}, Cannot assign PDU session to UPF because of resource "
                           f"constraints, terminating PDU session")
                self._log(message)
                self.terminate_pdu_session(session)

        if available_upf:
            if (self.active_sessions == (self.num_upf_instances * self.max_sessions_per_upf) -
                    self.scale_out_threshold - 1) and self.num_upf_instances < self.max_upf_instances:
                self.scale_out()

            message = f"Time: {np.ceil(self.current_time)}, UE sends PDU session {session_id} request to Compute Node"
            self._log(message)
            available_upf.add_session(session)
            self.active_sessions += 1
            self.update_free_slots()
            end_event = Event(EVENT_TERMINATE_PDU_SESSION, np.ceil(self.current_time) + duration)
            heapq.heappush(self.event_queue, end_event)

            message = (
                f"Time: {np.ceil(self.current_time)}, Compute Node allocates UPF {available_upf.upf_id} for PDU session "
                f"{session_id}")
            self._log(message)
            message = f"Time: {np.ceil(self.current_time)}, PDU Session {session_id} started on UPF {available_upf.upf_id}"
            self._log(message)

    def terminate_pdu_session(self, session):
        upf = next((upf for upf in self.upfs if session in upf.sessions), None)
        if upf:
            upf.remove_session(session)
            self.active_sessions -= 1
            self.update_free_slots()
            message = (f"Time: {np.ceil(self.current_time)}, PDU Session {session.session_id} "
                       f"terminated on UPF {upf.upf_id}")
            self._log(message)
            if self.migration_case == 1:
                # Case 1: No migration and uses scale-in threshold for termination
                if self.free_slots == self.scale_in_threshold and self.num_upf_instances >= self.min_upf_instances + 1:
                    self.scale_in(upf)

            if self.migration_case == 2:
                # Case 2: No migration and doesn't use scale-in threshold for termination
                self.scale_in(upf)

            if self.migration_case == 3:
                # Case 3: UPFs accept PDUs even after migration and uses scale-in threshold for termination
                sorted_upfs = sorted(self.upfs, key=lambda x: len(x.sessions), reverse=True)
                target_upf = next((u for u in sorted_upfs if
                                   u != upf and len(u.sessions) + len(upf.sessions) <= self.max_sessions_per_upf), None)

                if target_upf:
                    for s in upf.sessions:
                        target_upf.add_session(s)
                        upf.remove_session(s)
                        message = (f"Time: {np.ceil(self.current_time)}, PDU Session {s.session_id} "
                                   f"migrated from UPF {upf.upf_id} to UPF {target_upf.upf_id}")
                        self._log(message)

                if (len(upf.sessions) == 0 and self.free_slots >= self.scale_in_threshold and
                        self.num_upf_instances > self.min_upf_instances):
                    self.scale_in(upf)

            elif self.migration_case == 4:
                # Case 4: UPFs accept PDUs even after migration and doesn't use scale-in threshold
                sorted_upfs = sorted(self.upfs, key=lambda x: len(x.sessions), reverse=True)
                target_upf = next((u for u in sorted_upfs if
                                   u != upf and len(u.sessions) + len(upf.sessions) <= self.max_sessions_per_upf), None)

                if target_upf:
                    for s in upf.sessions:
                        target_upf.add_session(s)
                        upf.remove_session(s)
                        message = (f"Time: {np.ceil(self.current_time)}, PDU Session {s.session_id} "
                                   f"migrated from UPF {upf.upf_id} to UPF {target_upf.upf_id}")
                        self._log(message)

                if len(upf.sessions) == 0:
                    self.scale_in(upf)

            elif self.migration_case == 5:
                # Case 5: UPFs do not accept PDUs after migration and uses scale-in threshold
                sorted_upfs = sorted(self.upfs, key=lambda x: len(x.sessions), reverse=True)
                migrated_upfs = set()
                target_upf = None
                for u in sorted_upfs:
                    if u != upf and u not in migrated_upfs:
                        if len(u.sessions) + len(upf.sessions) <= self.max_sessions_per_upf:
                            target_upf = u
                            break

                if target_upf:
                    migrated_sessions = []
                    for s in upf.sessions:
                        migrated_sessions.append(s)
                        target_upf.add_session(s)
                        upf.remove_session(s)
                        message = (f"Time: {np.ceil(self.current_time)}, PDU Session {s.session_id} "
                                   f"migrated from UPF {upf.upf_id} to UPF {target_upf.upf_id}")
                        self._log(message)
                    migrated_upfs.add(upf)

                if (len(upf.sessions) == 0 and self.free_slots >= self.scale_in_threshold and
                        self.num_upf_instances > self.min_upf_instances):
                    self.scale_in(upf)

            elif self.migration_case == 6:
                # Case 6: UPFs do not accept PDUs after migration and doesn't use scale-in threshold
                sorted_upfs = sorted(self.upfs, key=lambda x: len(x.sessions), reverse=True)
                migrated_upfs = set()
                target_upf = None
                for u in sorted_upfs:
                    if u != upf and u not in migrated_upfs:
                        if len(u.sessions) + len(upf.sessions) <= self.max_sessions_per_upf:
                            target_upf = u
                            break

                if target_upf:
                    migrated_sessions = []
                    for s in upf.sessions:
                        migrated_sessions.append(s)
                        target_upf.add_session(s)
                        upf.remove_session(s)
                        message = (f"Time: {np.ceil(self.current_time)}, PDU Session {s.session_id} "
                                   f"migrated from UPF {upf.upf_id} to UPF {target_upf.upf_id}")
                        self._log(message)
                    migrated_upfs.add(upf)

                if len(upf.sessions) == 0:
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
            self.update_free_slots()
            message = f"Time: {np.ceil(self.current_time)}, Compute Node launches UPF {new_upf_id}"
            self._log(message)

    def scale_in(self, upf):
        """
        Scale in by terminating a UPF instance.

        :param upf: UPF instance to be terminated.
        """
        if upf.upf_id >= self.min_upf_instances:
            self.upfs.remove(upf)
            self.num_upf_instances -= 1
            self.update_free_slots()
            message = f"Time: {np.ceil(self.current_time)}, Compute Node terminates UPF {upf.upf_id}"
            self._log(message)

    def run(self):
        """
        Run the simulation.

        This method executes the simulation and generates plots for PDU count against simulation time
        and UPF count against simulation time.
        """

        pdu_counts = []  # List to store PDU counts
        upf_counts = []  # List to store UPF counts
        active_pdu_counts = []  # List to store active PDU counts
        active_upf_counts = []  # List to store active UPF counts
        time_points = []  # List to store time points

        pdu_file = open('pdus.csv', 'w', newline='')
        pdu_writer = csv.writer(pdu_file)
        pdu_writer.writerow(['Time', 'PDUs'])

        upf_file = open('upfs.csv', 'w', newline='')
        upf_writer = csv.writer(upf_file)
        upf_writer.writerow(['Time', 'UPFs'])

        active_pdu_file = open('active_pdus.csv', 'w', newline='')
        active_pdu_writer = csv.writer(active_pdu_file)
        active_pdu_writer.writerow(['Time', 'Active PDUs'])

        active_upf_file = open('active_upfs.csv', 'w', newline='')
        active_upf_writer = csv.writer(active_upf_file)
        active_upf_writer.writerow(['Time', 'Active UPFs'])

        # Schedule the initial PDU session generation
        generation_event = Event(EVENT_GENERATE_PDU_SESSION, 0)
        heapq.heappush(self.event_queue, generation_event)

        while np.ceil(self.current_time) < self.simulation_time or self.event_queue:
            if not self.event_queue:
                break

            event = heapq.heappop(self.event_queue)
            self.current_time = event.time

            pdu_counts.append(self.session_counter)  # Record PDU count
            upf_counts.append(self.next_upf_id)  # Record UPF count
            active_pdu_counts.append(self.active_sessions)  # Record active PDU count
            active_upf_counts.append(self.num_upf_instances)  # Record active UPF count
            time_points.append(np.ceil(self.current_time))  # Record time

            pdu_writer.writerow([np.ceil(self.current_time), self.session_counter])
            upf_writer.writerow([np.ceil(self.current_time), self.next_upf_id])
            active_pdu_writer.writerow([np.ceil(self.current_time), self.active_sessions])
            active_upf_writer.writerow([np.ceil(self.current_time), self.num_upf_instances])

            if event.event_type == EVENT_GENERATE_PDU_SESSION:
                self.generate_pdu_session()

                # Schedule the next PDU session generation
                next_generation_time = np.ceil(
                    self.current_time + (np.random.exponential(1 / self.arrival_rate) * 1000))
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
            message = f"Time: {np.ceil(self.current_time)}, Compute Node terminates UPF {upf.upf_id}"
            self._log(message)

        pdu_file.close()
        upf_file.close()
        active_pdu_file.close()
        active_upf_file.close()

        self._log(f"Simulation completed. Total PDU sessions processed: {self.session_counter}. "
                  f"Total UPFs deployed: {self.next_upf_id}.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Event-based scheduler simulation")
    parser.add_argument("--upf_case", type=int, default=2, help="Case for UPF sorting")
    parser.add_argument("--max-upf-instances", type=int, default=110, help="Maximum number of UPF instances (L)")
    parser.add_argument("--min-upf-instances", type=int, default=1, help="Minimum number of UPF instances (M)")
    parser.add_argument("--max-sessions-per-upf", type=int, default=8, help="Maximum number of sessions per UPF (C)")
    parser.add_argument("--scale-out-threshold", type=int, default=3, help="Scale-out threshold (T1)")
    parser.add_argument("--scale-in-threshold", type=int, default=13, help="Scale-in threshold (T2)")
    parser.add_argument("--simulation-time", type=int, default=10000, help="Simulation time in milliseconds")
    parser.add_argument("--arrival_rate", type=int, default=500, help="Inter-arrival rate in seconds (λ)")
    parser.add_argument("--mu", type=int, default=10, help="parameter for session duration in seconds (µ)")
    parser.add_argument("--migration_case", type=int, default=6, help="Case for session migration")
    parser.add_argument("--output-file", type=str, default="simulation.log", help="File to write simulation outputs")

    args = parser.parse_args()

    scheduler = Scheduler(args.upf_case, args.max_upf_instances, args.min_upf_instances, args.max_sessions_per_upf,
                          args.scale_out_threshold, args.scale_in_threshold, args.simulation_time, args.arrival_rate,
                          args.mu, args.migration_case, args.output_file)
    scheduler.run()
