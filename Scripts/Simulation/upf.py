class UPF:
    """
    Represents a UPF (User Plane Function) in the simulation.
    """

    def __init__(self, upf_id, throughput_capacity):
        """
        Initialize a UPF with its ID and throughput capacity.

        :param upf_id: ID of the UPF.
        :param throughput_capacity: Throughput capacity of the UPF.
        """
        self.upf_id = upf_id
        self.throughput_capacity = throughput_capacity
        self.sessions = []
        self.current_throughput = 0

    def add_session(self, session):
        """
        Add a session to the UPF.

        :param session: Session object to be added.
        """
        self.sessions.append(session)
        self.current_throughput += session.throughput

    def remove_session(self, session):
        """
        Remove a session from the UPF.

        :param session: Session object to be removed.
        """
        self.sessions.remove(session)
        self.current_throughput -= session.throughput

    def is_busy(self):
        """
        Check if the UPF has any active sessions.

        :return: True if the UPF has active sessions, False otherwise.
        """
        return len(self.sessions) > 0

    def has_capacity_for(self, throughput):
        """
        Check if the UPF has capacity for an additional throughput.

        :param throughput: Throughput of the new session.
        :return: True if there is enough capacity, False otherwise.
        """
        return self.current_throughput + throughput <= self.throughput_capacity
