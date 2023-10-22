
from ArraySet import ArraySet
from LinkedSet import LinkedSet


def main():
    arr_set1 = ArraySet()
    arr_set1.add(2)
    arr_set1.add(3)
    arr_set1.add(6)
    arr_set1.add(5)
    arr_set1.remove(6)

    arr_set2 = ArraySet()
    arr_set2.add(1)
    arr_set2.add(2)
    arr_set2.add(5)
    arr_set2.add(4)
    arr_set2.remove(2)
    arr_set2.add(6)
    arr_set2.add(8)

    print("Array Set")
    print("Array Set1: ", arr_set1)
    print("Array Set2: ", arr_set2)
    print("Intersection: ")
    print(arr_set1.intersection(arr_set2))
    print("Union: ")
    print(arr_set1.union(arr_set2))
    print()


    link_set1= LinkedSet()
    link_set1.add(1)
    link_set1.add(2)
    link_set1.add(3)
    link_set1.add(4)
    link_set1.add(5)
    link_set1.remove(5)

    link_set2= LinkedSet()
    link_set2.add(5)
    link_set2.add(6)
    link_set2.add(7)
    link_set2.add(8)
    link_set2.add(9)
    link_set2.remove(8)
    
    print("Linked Set")
    print("Linked Set1: ", link_set1)
    print("Linked Set2: ", link_set2)

    print("Intersection: ")
    print(link_set1.intersection(link_set2))
    print("Union: ")
    print(link_set1.union(link_set2))

    
main()

