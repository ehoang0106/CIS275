class Node:
    """ represents a singly-linked node """
    def __init__(self, data, next=None):
        self._data = data
        self._next = next


def length(head):
    
    count = 0
    current = head

    while current is not None:
        count+=1
        current = current._next

    return count


def num_times(head, target):
    count = 0
    current = head
    

    while current is not None:
        if current._data == target:
            count+=1

        current = current._next

    return count