from LinkedBST import LinkedBST



def main():

    bst = LinkedBST()

    for i in [20, 30, 50, 60, 70, 40, 80]:
        bst.add(i)


    print("Find 80 in tree:")
    bst.find(80)

    print("Find 20 in tree:")
    bst.find(20)

    print("Find 60 in tree:")
    bst.find(60)

    print("\nPreorder: ")
    bst.preorder()

    print("\nPostorder: ")
    bst.postorder()


main()