from AbstractCollection import AbstractCollection
from Node import Node

class LinkedQueue(AbstractCollection):

    """ A linked list-based queue implementation """
    def __init__(self):
        self._front = None
        self._rear = None
        AbstractCollection.__init__(self)

    def add(self, new_item):
        """ Add 'new_item' to the back of the queue """
        new_node = Node(new_item)
        if self.is_empty():
            """ No nodes in the linked list """
            self._front = new_node
            self._rear = new_node
        else:
            """ At least one node already in the linked list. Point the last node to it """
            self._rear._next = new_node
            self._rear = new_node
        self._numitems += 1

    def pop(self):
        """
        Precondition: Queue is not empty
        Postcondition: Queue has one less item in it
        Raises: ValueError if Queue is empty
        :return: The item previously at the front of the queue
        """
        if self.is_empty():
            raise ValueError("Queue is empty!")
        return_item = self._front._data
        self._front = self._front._next

        if self._front is None:
            """ Queue had only one item in it """
            self._rear = None

        self._numitems -= 1
        return return_item

    def clear(self):
        """ Makes self empty """
        self._front = None
        self._rear = None
        self._numitems = 0

    def peek(self):
        """ Returns the entry at the front of the Queue
        Precondition: Queue is not empty
        Raises: ValueError if the Queue is empty
        """
        if self.is_empty():
            raise ValueError("Queue is empty!")
        return self._front._data


    def __str__(self):
        """ For testing purposes only """
        return_string = "Front:"
        probe = self._front
        while probe is not None:
            return_string += " " + str(probe._data)
            probe = probe._next

        return_string += " :Back"
        return return_string