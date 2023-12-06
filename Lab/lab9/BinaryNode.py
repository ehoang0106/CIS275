class BinaryNode:
	""" Represents a Node in a binary tree """

	def __init__(self, data, left=None, right=None):
		""" By default, this Node will not have any children """

		self.data = data
		self.left = left
		self.right = right