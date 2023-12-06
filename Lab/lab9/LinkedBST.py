from AbstractCollection import AbstractCollection
from BinaryNode import BinaryNode


class LinkedBST(AbstractCollection):
	""" A linked binary search tree implementation which uses Nodes """

	def __init__(self):
		self._root = None
		AbstractCollection.__init__(self)

	def find(self, item):
		""" Return data if the item is found or 'None' otherwise """
		#set count visited = 0

		self._visited_count = 0

		def recurse(node):
			if node is None:
				# First Base Case: Item was not found
				return None
			else:
				self._visited_count += 1


			if item == node.data:
				# Second Base Case: node contains the item!
				return node.data
			
			elif item < node.data:
				# Recursive Step 1: Move left
				return recurse(node.left)
			else:
				# Recursive Step 2: Move right
				return recurse(node.right)

		item_found = recurse(self._root)
		print(f"Search complete. {self._visited_count} Nodes visited")

		return item_found

	def add(self, item):
		def recurse(node):
			""" Recursive inner function to find 'item's correct location
			'node' is the root of the tree or subtree being added to """
			if item < node.data:
				# New item being added is less. Go left once if needed
				if node.left is None:
					node.left = BinaryNode(item)
				else:
					recurse(node.left)

			# new item is greater or equal to root, go right if needed
			elif node.right is None:
				node.right = BinaryNode(item)
			else:
				recurse(node.right)

		if self.is_empty():
			# Tree is empty, 'item' becomes the new root
			self._root = BinaryNode(item)
		else:
			# Tree is not empty. Find item's location
			recurse(self._root)

		self._size += 1

	def inorder(self):
		""" Prints the tree with an inorder traversal """
		def recurse(node):
			if node is not None:
				recurse(node.left)
				print(node.data, end=" ")
				recurse(node.right)

		recurse(self._root)

	def preorder(self):

		def recurse(node):
			if node is not None:
				print(node.data, end=" ")
				recurse(node.left)
				recurse(node.right)
		recurse(self._root)


	def postorder(self):

		def recurse(node):
			if node is not None:
				recurse(node.left)
				recurse(node.right)
				print(node.data, end=" ")
		recurse(self._root)

