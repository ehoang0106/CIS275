from ArrayStack import ArrayStack



def check_binary(input_str):
    
    stack = ArrayStack()

    for char in input_str:

        if char not in '01':
            return "Wrong input only input 0 and 1!"
        
        if not stack.is_empty():
            if stack.peek() != char:
                stack.pop()
                continue
        
        stack.push(char)

    if stack.is_empty():
        return "Balanced!"
    else:
        return "Not balanced!"

def main():
    while True:
        binary_str = input("Enter binary string, 'q' to quit: ")

        if binary_str == 'q':
            break

        if len(binary_str) == 2 and binary_str == '01' or len(binary_str) == 2 and binary_str == '10':
            print("Not balanced!")
            continue

        result = check_binary(binary_str)

        print(result)

        

main()