from Contact import Contact
from Node import Node


class ContactList:

    def __init__(self):
        self._head = None


    

    def add(self, name, new_number):
        new_contact = Contact(name, new_number)
        new_node = Node(new_contact)


        if self._head is None or self._head._data._name > name:
            new_node._next = self._head
            self._head = new_node
        else:

            current = self._head
            while current._next is not None and current._next._data._name < name:
                current = current._next

            new_node._next = current._next
            current._next = new_node
        
        print(f"Successfully added contact {name} with phone number {new_number} in contact list!")


    def remove(self, name):
        if self._head is None:
            print("There is no contact to remove!\n")
            return
        
         #remove the very first contact(contact is a head)
        if self._head._data._name == name:
            self._head = self._head._next
            print(f"{name} has been removed from contact list!\n")
            return
        
        #remove the contact in the middle of the list (contact that is not the head)
        current = self._head
        while current._next and current._next._data._name != name:
            current = current._next
        if current._next:
            current._next = current._next._next
            print(f"{name} has been removed from the contact list!\n")
        



    def change_phone_number(self, name, new_number):
        current = self._head

        while current:

            if current._data._name == name:
                current._data._phone_number = new_number
                print(f"{name}'s phone number has been updated. New number is: {new_number}\n")
                return
            
            
            current = current._next
        
        

    def name_exists(self, name):
        current = self._head
        while current:
            if current._data._name == name:
                return True
            current = current._next
        
        return False

    def __str__(self):

        if self._head is None:
            return "There is no contact in the list!\n"
        
        contacts = []
        current = self._head
        

        while current:
            contacts.append(str(current._data))
            current = current._next
        
        return "\n".join(contacts)