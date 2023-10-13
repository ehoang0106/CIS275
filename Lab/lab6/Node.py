class Node:
	""" Represents a Node in a singly-linked list """

	def __init__(self, data, next=None):
		""" By default, this Node will not link to another Node """

		self.data = data
		self.next = next
