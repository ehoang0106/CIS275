
from ContactList import ContactList


def main():
    
    contacts = ContactList()

    while True:
        print()
        print("Choose:")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Change phone number")
        print("4. Print contacts")
        print("5 Quit")

        choose = input("Enter option: ")
       
        if choose == "1":
            name = input("Enter name of the contact: ")
            if contacts.name_exists(name):
                print(f"{name} is already existed in the contact list. Please use option 3 to update phone number!\n")

            else:
                phone_number = input("Enter phone number: ")
                contacts.add(name, phone_number)


        elif choose == "2":
            name = input("Enter name of the contact you want to remove: ")
            if contacts.name_exists(name):
                contacts.remove(name)
            else:
                print(f"{name} not found in the contact!")

        elif choose == "3":
            name = input("Enter updating name: ")
            if contacts.name_exists(name):

                phone_number = input("Enter updating phone number: ")
                contacts.change_phone_number(name, phone_number)
            else:
                print(f"{name} not found in the contact!")
        
        elif choose == "4":
            print(contacts)

        elif choose == "5":
            break
        else:
            print("Invalid option. Try again!")
        



main()