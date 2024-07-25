import heapq
import csv
import os
import random
import numpy as np
from event import Event
from pdu_session import PDUSession
from upf import UPF

EVENT_GENERATE_PDU_SESSION = 1
EVENT_TERMINATE_PDU_SESSION = 2


class Scheduler:
    """
    Implements the event-based scheduler simulation.
    """

    def __init__(self, run_id, upf_case, max_upf_instances, min_upf_instances, max_sessions_per_upf,
                 scale_out_threshold,
                 scale_in_threshold, simulation_time, arrival_rate, mu, migration_case, output_file, seed=None):
        """
        Initialize the scheduler with simulation parameters.

        :param run_id: ID of simulation run
        :param seed: Seed for reproducibility of the experiment
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
        self.run_id = run_id
        self.seed = seed
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
        self.rejected_sessions = []  # List to store rejected sessions and their times
        self.busy_upfs = 0  # Number of UPFs with active PDU sessions
        self.idle_upfs = 0  # Number of UPFs without active PDU sessions
        self.output_file = output_file

        if self.seed is not None:
            random.seed(self.seed)
            np.random.seed(self.seed)

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

    def update_active_sessions(self):
        """
        Update the number of active sessions in the system.
        """
        self.active_sessions = sum(len(upf.sessions) for upf in self.upfs)

    def update_upf_status(self):
        """
        Update the number of busy and idle UPFs in the system.
        """
        self.busy_upfs = sum(1 for upf in self.upfs if upf.is_busy())
        self.idle_upfs = self.num_upf_instances - self.busy_upfs

    def calculate_utilization(self):
        """
        Calculate the utilization of the system.
        Utilization U = ∑(i,j)∈S (i / (j * C)) * p_{i,j}
        where:
        - i is the number of sessions at that instant
        - j is the number of UPFs at that instant
        - C is the capacity of each UPF instance
        - p_{i,j} is assumed to be 1 as each session contributes fully to utilization
        """
        total_utilization = 0
        for upf in self.upfs:
            sessions = len(upf.sessions)
            total_utilization += sessions / (self.num_upf_instances * self.max_sessions_per_upf)
        return total_utilization

    def log_utilization(self):
        """
        Log the current utilization to a CSV file.
        """
        utilization = self.calculate_utilization()
        file_path = f'../Data/utilization_{self.run_id}.csv'
        file_exists = os.path.isfile(file_path)
        with open(file_path, 'a', newline='') as util_file:
            util_writer = csv.writer(util_file)
            if not file_exists:
                util_writer.writerow(['Time', 'Utilization'])
            util_writer.writerow([np.ceil(self.current_time), utilization])

    def get_upf_with_lowest_sessions(self):
        """
        Get the UPF with the lowest number of sessions, while respecting the max_sessions_per_upf limit.
        If multiple UPFs have the same lowest number of sessions, randomly select one.
        """
        upfs_under_limit = [upf for upf in self.upfs if len(upf.sessions) < self.max_sessions_per_upf]
        if not upfs_under_limit:
            return None

        upfs_sorted = sorted(upfs_under_limit, key=lambda upf: len(upf.sessions))
        lowest_sessions_upfs = [upf for upf in upfs_sorted if len(upf.sessions) == len(upfs_sorted[0].sessions)]
        return random.choice(lowest_sessions_upfs)

    def get_upf_with_highest_sessions(self):
        """
        Get the UPF with the highest number of sessions, while respecting the max_sessions_per_upf limit.
        If multiple UPFs have the same highest number of sessions, randomly select one.
        """
        upfs_under_limit = [upf for upf in self.upfs if len(upf.sessions) < self.max_sessions_per_upf]
        if not upfs_under_limit:
            return None

        upfs_sorted = sorted(upfs_under_limit, key=lambda upf: len(upf.sessions), reverse=True)
        highest_sessions_upfs = [upf for upf in upfs_sorted if len(upf.sessions) == len(upfs_sorted[0].sessions)]
        return random.choice(highest_sessions_upfs)

    def generate_pdu_session(self):
        """
        Generate a new PDU session event.
        """
        global available_upf
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
        elif self.upf_case == 3:
            available_upf = self.get_upf_with_highest_sessions() if self.upfs else None
        else:
            message = f"Time: {np.ceil(self.current_time)}, No UPF available"
            self._log(message)

        # If no available UPF, scale out if possible
        if not available_upf:
            if self.num_upf_instances < self.max_upf_instances:
                self.scale_out()
                available_upf = self.upfs[-1]
            else:
                self.rejected_sessions.append((session_id, np.ceil(self.current_time)))
                message = f"Time: {np.ceil(self.current_time)}, Cannot scale out due to maximum UPF instances reached"
                self._log(message)
                message = (f"Time: {np.ceil(self.current_time)}, Cannot assign PDU session to UPF because of resource "
                           f"constraints, terminating PDU session")
                self._log(message)
                return

        if available_upf:
            if (self.active_sessions == (self.num_upf_instances * self.max_sessions_per_upf) -
                    self.scale_out_threshold - 1) and self.num_upf_instances < self.max_upf_instances:
                self.scale_out()

            message = f"Time: {np.ceil(self.current_time)}, UE sends PDU session {session_id} request to Compute Node"
            self._log(message)
            available_upf.add_session(session)
            self.update_active_sessions()
            self.update_free_slots()
            self.update_upf_status()
            self.log_utilization()
            end_event = Event(EVENT_TERMINATE_PDU_SESSION, np.ceil(self.current_time) + duration)
            heapq.heappush(self.event_queue, end_event)

            message = (
                f"Time: {np.ceil(self.current_time)}, Compute Node allocates UPF {available_upf.upf_id} for PDU session"
                f"{session_id}")
            self._log(message)
            message = (f"Time: {np.ceil(self.current_time)}, PDU Session {session_id} "
                       f"started on UPF {available_upf.upf_id}")
            self._log(message)

            file_path = f'../Data/session_durations_{self.run_id}.csv'
            file_exists = os.path.isfile(file_path)
            file_empty = os.path.getsize(file_path) == 0 if file_exists else True
            with open(file_path, 'a', newline='') as duration_file:
                duration_writer = csv.writer(duration_file)
                if file_empty:
                    duration_writer.writerow(['Session ID', 'Duration (seconds)'])
                duration_writer.writerow([session_id, np.ceil(duration / 1000)])

    def terminate_pdu_session(self, session):
        upf = next((upf for upf in self.upfs if session in upf.sessions), None)
        if upf:
            upf.remove_session(session)
            self.update_active_sessions()
            self.update_free_slots()
            self.update_upf_status()
            self.log_utilization()
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

                if self.free_slots == self.scale_in_threshold and self.num_upf_instances >= self.min_upf_instances + 1:
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

                if self.free_slots == self.scale_in_threshold and self.num_upf_instances >= self.min_upf_instances + 1:
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
        new_upf_id = self.next_upf_id
        self.next_upf_id += 1
        new_upf = UPF(new_upf_id)
        self.upfs.append(new_upf)
        self.num_upf_instances += 1
        self.update_free_slots()
        self.update_upf_status()
        self.log_utilization()
        message = f"Time: {np.ceil(self.current_time)}, Compute Node launches UPF {new_upf_id}"
        self._log(message)

    def scale_in(self, upf):
        """
        Scale in by terminating a UPF instance.

        :param upf: UPF instance to be terminated.
        """
        self.upfs.remove(upf)
        self.num_upf_instances -= 1
        self.update_free_slots()
        self.update_upf_status()
        self.log_utilization()
        message = f"Time: {np.ceil(self.current_time)}, Compute Node terminates UPF {upf.upf_id}"
        self._log(message)

    def run(self):
        """
        Run the simulation.

        This method executes the simulation.
        """

        pdu_counts = []  # List to store PDU counts
        upf_counts = []  # List to store UPF counts
        active_pdu_counts = []  # List to store active PDU counts
        free_slots = []  # List to store free slots
        time_points = []  # List to store time points
        busy_upf_counts = []  # List to store busy UPF counts
        idle_upf_counts = []  # List to store idle UPF counts
        inter_arrival_times = []  # List to store inter-arrival times
        deployed_upf_counts = []

        pdu_file = open(f'../Data/pdus_{self.run_id}.csv', 'w', newline='')
        pdu_writer = csv.writer(pdu_file)
        pdu_writer.writerow(['Time', 'PDUs'])

        upf_file = open(f'../Data/upfs_{self.run_id}.csv', 'w', newline='')
        upf_writer = csv.writer(upf_file)
        upf_writer.writerow(['Time', 'UPFs'])

        active_pdu_file = open(f'../Data/active_pdus_{self.run_id}.csv', 'w', newline='')
        active_pdu_writer = csv.writer(active_pdu_file)
        active_pdu_writer.writerow(['Time', 'Active PDUs'])

        free_slots_file = open(f'../Data/free_slots_{self.run_id}.csv', 'w', newline='')
        free_slots_writer = csv.writer(free_slots_file)
        free_slots_writer.writerow(['Time', 'Free Slots'])

        rejected_sessions_file = open(f'../Data/rejected_sessions_{self.run_id}.csv', 'w', newline='')
        rejected_sessions_writer = csv.writer(rejected_sessions_file)
        rejected_sessions_writer.writerow(['Time', 'Session ID'])

        busy_upf_file = open(f'../Data/busy_upfs_{self.run_id}.csv', 'w', newline='')
        busy_upf_writer = csv.writer(busy_upf_file)
        busy_upf_writer.writerow(['Time', 'Busy UPFs'])

        idle_upf_file = open(f'../Data/idle_upfs_{self.run_id}.csv', 'w', newline='')
        idle_upf_writer = csv.writer(idle_upf_file)
        idle_upf_writer.writerow(['Time', 'Idle UPFs'])

        inter_arrival_file = open(f'../Data/inter_arrival_times_{self.run_id}.csv', 'w', newline='')
        inter_arrival_writer = csv.writer(inter_arrival_file)
        inter_arrival_writer.writerow(['Inter-arrival Time'])

        utilization_file = open(f'../Data/utilization_{self.run_id}.csv', 'w', newline='')
        utilization_writer = csv.writer(utilization_file)
        utilization_writer.writerow(['Time', 'Utilization'])

        deployed_upf_file = open(f'../Data/deployed_upfs_{self.run_id}.csv', 'w', newline='')
        deployed_upf_writer = csv.writer(deployed_upf_file)
        deployed_upf_writer.writerow(['Time', 'Deployed UPFs'])

        # Schedule the initial PDU session generation
        initial_generation_time = 0
        generation_event = Event(EVENT_GENERATE_PDU_SESSION, initial_generation_time)
        heapq.heappush(self.event_queue, generation_event)

        while self.event_queue and np.ceil(self.current_time) < self.simulation_time:
            event = heapq.heappop(self.event_queue)
            self.current_time = event.time

            pdu_counts.append(self.session_counter)  # Record PDU count
            upf_counts.append(self.next_upf_id)  # Record UPF count
            active_pdu_counts.append(self.active_sessions)  # Record active PDU count
            time_points.append(np.ceil(self.current_time))  # Record time
            free_slots.append(self.free_slots)  # Record free slots
            busy_upf_counts.append(self.busy_upfs)  # Record busy UPF count
            idle_upf_counts.append(self.idle_upfs)  # Record idle UPF count
            deployed_upf_counts.append(self.num_upf_instances)

            pdu_writer.writerow([np.ceil(self.current_time), self.session_counter])
            upf_writer.writerow([np.ceil(self.current_time), self.next_upf_id])
            active_pdu_writer.writerow([np.ceil(self.current_time), self.active_sessions])
            free_slots_writer.writerow([np.ceil(self.current_time), self.free_slots])
            busy_upf_writer.writerow([np.ceil(self.current_time), self.busy_upfs])
            idle_upf_writer.writerow([np.ceil(self.current_time), self.idle_upfs])
            deployed_upf_writer.writerow([np.ceil(self.current_time), self.num_upf_instances])

            if event.event_type == EVENT_GENERATE_PDU_SESSION:
                self.generate_pdu_session()

                # Schedule the next PDU session generation
                next_generation_time = np.ceil(
                    self.current_time + (np.random.exponential(1 / self.arrival_rate) * 1000))
                if next_generation_time <= self.simulation_time:
                    generation_event = Event(EVENT_GENERATE_PDU_SESSION, next_generation_time)
                    heapq.heappush(self.event_queue, generation_event)
                    inter_arrival_time = next_generation_time - initial_generation_time
                    inter_arrival_times.append(inter_arrival_time)
                    inter_arrival_writer.writerow([inter_arrival_time])
                    initial_generation_time = next_generation_time

            elif event.event_type == EVENT_TERMINATE_PDU_SESSION:
                session = next(
                    (session for upf in self.upfs for session in upf.sessions if session.end_time == self.current_time),
                    None)
                if session:
                    self.terminate_pdu_session(session)

        for session_id, rejection_time in self.rejected_sessions:
            rejected_sessions_writer.writerow([rejection_time, session_id])

        # Terminate any remaining UPFs
        for upf in self.upfs:
            message = f"Time: {np.ceil(self.current_time)}, Compute Node terminates UPF {upf.upf_id}"
            self._log(message)

        pdu_file.close()
        upf_file.close()
        active_pdu_file.close()
        free_slots_file.close()
        rejected_sessions_file.close()
        busy_upf_file.close()
        idle_upf_file.close()
        inter_arrival_file.close()
        utilization_file.close()
        deployed_upf_file.close()

        self._log(f"Simulation completed. Total PDU sessions processed: {self.session_counter}. "
                  f"Total UPFs deployed: {self.next_upf_id}."
                  f"Rejected sessions: {len(self.rejected_sessions)}."
                  f"Accepted sessions: {self.session_counter - len(self.rejected_sessions)}.")

        sim_data = open(f'../Data/sim_data_{self.run_id}.csv', 'w', newline='')
        sim_data_writer = csv.writer(sim_data)
        sim_data_writer.writerow(
                ['Total PDU sessions processed', 'Rejected sessions', 'Accepted sessions'])
        sim_data_writer.writerow([self.session_counter, len(self.rejected_sessions),
                                  self.session_counter - len(self.rejected_sessions)])

