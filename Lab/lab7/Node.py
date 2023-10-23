class Node:
    """ Represents a singly linked node """

    def __init__(self, data, next=None):
        """ By default, this Node will not link to another Node """
        self._data = data
        self._next = next
