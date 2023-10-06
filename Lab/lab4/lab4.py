from Node import Node, length, num_times


def main():
    head = None

    while True:
        item = input("Enter item or 'q' to quit: ")
        if item == 'q':
            break

        head = Node(item, head)
        

    print(f"Length: {length(head)}")
    target = 'kh'

    print(f"Number of times '{target}' appears: {num_times(head,target)} time(s)")

main()


