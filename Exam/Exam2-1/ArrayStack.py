from AbstractStack import AbstractStack
from Array import Array


class ArrayStack(AbstractStack):
	""" An array-based implementation of a stack"""

	DEFAULT_CAPACITY = 10

	def __init__(self):
		self._items = Array(ArrayStack.DEFAULT_CAPACITY)
		AbstractStack.__init__(self)

	def peek(self):
		""" Return item on top of the stack
		Precondition: Stack is not empty
		Raises: KeyError if the stack is empty """
		if self.is_empty():
			raise KeyError("Stack is empty, can't peek!")
		return self._items[self._size - 1]

	def push(self, item):
		""" Adds 'item' to top of the stack """

		# TODO Resize array if necessary
		if self._size == ArrayStack.DEFAULT_CAPACITY:
			raise KeyError("Stack is full!")

		self._items[self._size] = item
		self._size += 1

	def pop(self):
		""" Remove and return item on top of the stack
		Precondtion: Stack is not empty
		Raise: KeyError if the stack is empty """
		if self.is_empty():
			raise KeyError("Stack is empty, can't pop!")

		return_item = self._items[len(self) - 1]
		self._items[len(self) - 1] = None
		self._size -= 1
		return return_item

	def clear(self):
		""" Makes self empty """
		self._items = Array(ArrayStack.DEFAULT_CAPACITY)
		self._size = 0

	def print_stack(self):
		""" Prints all items in the stack, for testing purposes only """
		for i in range(self._size - 1, -1, -1):
			print(self._items[i])