class PDUSession:
    """
    Represents a PDU session in the simulation.
    """

    def __init__(self, session_id, start_time, duration, throughput):
        """
        Initialize a PDU session with its ID, start time, duration, and throughput.

        :param session_id: ID of the session.
        :param start_time: Start time of the session.
        :param duration: Duration of the session.
        :param throughput: Throughput of the session.
        """
        self.session_id = session_id
        self.start_time = start_time
        self.duration = duration
        self.end_time = start_time + duration
        self.throughput = throughput
