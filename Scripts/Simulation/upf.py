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

    def is_busy(self):
        """
        Check if the UPF has any active sessions.

        :return: True if the UPF has active sessions, False otherwise.
        """
        return len(self.sessions) > 0
