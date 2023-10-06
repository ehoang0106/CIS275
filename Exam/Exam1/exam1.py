from LinkedList import LinkedList


def main():
    list1 = LinkedList()
    list2 = LinkedList()

    list1.print_list()
    list2.print_list()

    list1.add_to_back(2)
    list1.add_to_front(1)
    list1.add_to_back(3)


    list2.add_to_back(5)
    list2.add_to_front(4)
    list2.add_to_back(6)


    print("List 1: ", end=" ")
    list1.print_list()
    
    print(f"Length of list 1: {len(list1)}")



    print("List 2: ", end= " ")
    list2.print_list()

    print(f"Length of list 2: {len(list2)}")
    

    print("Compare List 1 and 2: ")
    if list1 == list2:
        print("List 1 is equal List 2\n")
    else:
        print("List 1 is not equal List 2\n")

    list3 = list1 + list2
    print("List 3: ", end=" ")
    list3.print_list()
    print(f"Length of list 3: {len(list3)}")


    list3.remove_from_front()
    print("List 3 removed from front: ", end= " ")
    list3.print_list()

    
    list4 = LinkedList()
    list5 = LinkedList()


    list4.add_to_back(7)
    list4.add_to_front(8)
    list4.add_to_back(9)


    list5.add_to_back(7)
    list5.add_to_front(8)
    list5.add_to_back(9)


    print("List 4: ", end=" ")
    list4.print_list()

    print("List 5: ", end= " ")
    list5.print_list()



    print("Compare List 4 and 5: ")
    if list4 == list5:
        print("List 4 is equal List 5\n")
    else:
        print("List 4 is not equal List 5\n")
    
    
main()