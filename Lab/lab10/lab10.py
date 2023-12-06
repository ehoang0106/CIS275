import random

from MaxHeap import MaxHeap


def main():

    random_list = []

    for i in range(100):
        random_list.append(random.randint(1,100))
    
    k = int(input("Enter K (between 1 and 100): "))
    if k > 100:
        k = 100
        print("k value adjusted to 100 as it cannot exceed the number of elements in the heap.")

    max_heap = MaxHeap()

    for i in random_list:
        max_heap.add(i)


    largest_nums = []

    for i in range(k):
        largest_nums.append(max_heap.pop())


    print(f"The {k}-largest number are: {largest_nums}")


main()