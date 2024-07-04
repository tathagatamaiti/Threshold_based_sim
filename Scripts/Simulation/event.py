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
