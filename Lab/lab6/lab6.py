from LinkedStack import LinkedStack

def is_balanced(exp):
    s = LinkedStack()

    for character in exp:
        if character in ['(','[','{']:
            s.push(character)

        elif character == '}':
            if s.is_empty() or s.peek() != '{':
                return False
            else:
                s.pop()

        elif character == ')':
            if s.is_empty() or s.peek() != '(':
                return False
            else:
                s.pop()
        elif character == ']':
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

    for symbol in symbols:
        if symbol.isdigit():
            postfix.append(symbol)

        elif symbol in "+-*/^":
            while (not stack.is_empty() and stack.peek() in "+-*/^" and
                   precedence[symbol] <= precedence[stack.peek()]):
                postfix.append(stack.pop())
            stack.push(symbol)

        elif symbol == '(':
            stack.push(symbol)

        elif symbol == ')':
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