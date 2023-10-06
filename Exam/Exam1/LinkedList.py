from Node import Node


class LinkedList:
	def __init__(self):
		self._head = None
	

	def __len__(self):
		""" Return the number of Nodes in the list """
		count = 0
		probe = self._head
		while probe is not None:
			count += 1
			probe = probe.next
		return count
	

	def add_to_back(self, data):

		new_node = Node(data)

		if not self._head:
			self._head = new_node
			print(f"Sucessfully added {data} to back of a list!\n")
		else:
			probe = self._head
			while probe._next:
				probe = probe._next
			probe._next = new_node
			print(f"Sucessfully added {data} to back of a list!\n")
			
		

	def __add__(self, other):
		
		new_list = LinkedList()
		probe = self._head

		while probe:
			new_list.add_to_back(probe._data)
			probe = probe._next
		

		probe = other._head

		while probe:
			new_list.add_to_back(probe._data)
			probe = probe._next
		
		
		return new_list


	def remove_from_front(self):
		if not self._head:
			print("Cannot remove any data in a empty list!\n")
		else:
			removed_data =self._head._data
			self._head = self._head._next
			print(f"Successfully removed {removed_data} from front of the list!")





	def __eq__(self, other):
		if type(self) != type(other):
			return False
		if len(self) != len(other):
			return False
		probe1 = self._head
		probe2 = other._head
		while probe1 is not None:
			if probe1.data != probe2.data:
				return False
			probe1 = probe1.next
			probe2 = probe2.next
		return True

	def add_to_front(self, data):
		""" Add a new Node to the front of the LinkedList, with 'data' as its data attribute """
		self._head = Node(data, self._head)
		print(f"Sucessfully added {data} to front of a list!\n")


	def print_list(self):
		""" Print all the data in this linked list """

		if not self._head:
			print("List is empty!\n")
		else:

			probe = self._head
			while probe is not None:
				print(probe.data, end=" ")
				probe = probe.next
		
			print()
