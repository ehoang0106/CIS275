from AbstractQueue import ArrayQueue



def main():
    queue = ArrayQueue()

    #add more than 10 into queue
    for i in range(13):
        queue.add(i)


    queue.print_queue()
    print(f"Popped: {queue.pop()}")
    print(f"Peeked: {queue.peak()}")

    queue.clear()

    print("Cleared queue: ")
    queue.print_queue()


main()