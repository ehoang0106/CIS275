from AbstractCollection import AbstractCollection


class AbstractStack(AbstractCollection):

	def __init__(self):
		""" Calls the superclass constructor """
		AbstractCollection.__init__(self)

	def __add__(self, other):
		""" Although inherited from AbstractCollection, we don't want it to be """
		raise TypeError("Cannot add two stacks together")

	def __str__(self):
		""" The client is printing the stack """
		return "The value at the top of the stack is " + str(self.peek())
