from ArrayStack import ArrayStack

def main():
    current_val = 0
    redo_stack = ArrayStack()
    undo_stack = ArrayStack()

    while True:
        print(f"Current value: {current_val}")
        num = input("Enter a number, 'u' to undo, 'r' to redo, 'q' to quit: ").lower()

        if num == "u":
            if not undo_stack.is_empty():
                redo_stack.push(current_val)
                current_val = undo_stack.pop()
            else:
                print("No more actions to undo!")

        elif num == "r":
            if not redo_stack.is_empty():
                undo_stack.push(current_val)
                current_val = redo_stack.pop()

        elif num == "q":
            break
        
        else:
            try:
                
                num = float(num)
                operation = input("Enter operation (+, -, *, /): ")
                previous_val = current_val  

                if operation == "+":
                    current_val += num
                elif operation == "-":
                    current_val -= num
                elif operation == "*":
                    current_val *= num
                elif operation == "/":
                    if num == 0:
                        print("Cannot divide by 0")
                        continue
                    else:
                        result = current_val / num
                        
                        if result.is_integer():
                            current_val = int(result)
                        else:
                            current_val = result

                else:
                    print("Invalid operation!")
                    continue

                #clear stack
                redo_stack.clear()

                #push previous val to undo tack
                undo_stack.push(previous_val)

                print(f"{previous_val} {operation} {num} = {current_val}\n")

            except ValueError:
                print("Invalid input! Please enter a number.")

main()
