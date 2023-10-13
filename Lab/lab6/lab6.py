from LinkedStack import LinkedStack

def is_balanced(exp):
    s = LinkedStack()

    for symbol in exp:
        if symbol in ['(','[','{']:
            s.push(symbol)

        elif symbol == '}':
            if s.is_empty() or s.peek() != '{':
                return False
            else:
                s.pop()

        elif symbol == ')':
            if s.is_empty() or s.peek() != '(':
                return False
            else:
                s.pop()
        elif symbol == ']':
            if s.is_empty() or s.peek() != '[':
                return False
            else:
                s.pop()
    return s.is_empty()

def convert_to_postfix(infix_exp):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    postfix = []

    stack = LinkedStack()

    symbols = []
    current_symbol =""


    for i in infix_exp:
        if i in "+-*/^()":
            if current_symbol:
                symbols.append(current_symbol)
            symbols.append(i)
            current_symbol = ""

        elif i.isspace():
            if current_symbol:
                symbols.append(current_symbol)
            current_symbol = ""
        else:
            current_symbol += i

    if current_symbol:
        symbols.append(current_symbol)

    for character in symbols:
        if character.isdigit():
            postfix.append(character)

        elif character in "+-*/^":
            while (not stack.is_empty() and stack.peek() in "+-*/^" and precedence[character] <= precedence[stack.peek()]):
                postfix.append(stack.pop())
            stack.push(character)

        elif character == '(':
            stack.push(character)

        elif character == ')':
            while (not stack.is_empty() and stack.peek() != '('):
                postfix.append(stack.pop())
            if not stack.is_empty() and stack.peek() == '(':
                stack.pop()

    while not stack.is_empty():
        postfix.append(stack.pop())

    return ' '.join(postfix)


def main():
    while True:
        infix_exp = input("Enter infix expression or type 'q' to exit: ")
        if infix_exp == 'q':
            break

        if is_balanced(infix_exp):
            postfix_exp = convert_to_postfix(infix_exp)
            print(f"Postfix: {postfix_exp}")
        else:
            print("Expression is not balanced!")

main()