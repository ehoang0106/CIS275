from Node import Node
from AbstractStack import AbstractStack


class LinkedStack(AbstractStack):
	""" An linked-list-based implementation of a stack"""

	def __init__(self):
		self._items = None
		AbstractStack.__init__(self)

	def peek(self):
		""" Return item on top of the stack
		Precondition: Stack is not empty
		Raises: KeyError if the stack is empty """
		if self.is_empty():
			raise KeyError("Stack is empty, can't peek!")
		return self._items.data

	def push(self, item):
		""" Adds 'item' to top of the stack """

		self._items = Node(item, self._items)
		self._size += 1

	def pop(self):
		""" Remove and return item on top of the stack
		Precondtion: Stack is not empty
		Raise: KeyError if the stack is empty """
		if self.is_empty():
			raise KeyError("Stack is empty, can't pop!")

		return_item = self._items.data
		self._items = self._items.next
		self._size -= 1
		return return_item

	def clear(self):
		""" Makes self empty """
		self._items = None
		self._size = 0

	def print_stack(self):
		probe = self._items
		while probe:
			print(probe.data)
			probe = probe.next
