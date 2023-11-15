from .historytracker import History

import string


def welcome():
    print("WELCOME TO COMMANDLINE CALCULATOR!!")
    print()


def is_valid(inp):
    if not inp:
        return True

    valid_char = set(string.digits + "+-*/=><(). ")
    operators = set("+-*/%=<>")
    stack = []

    for i, char in enumerate(inp):
        if char not in valid_char:
            return False
        if i == 0 and char in operators:
            return False  # Disallow starting with an operator

        if char in "({[":
            stack.append(char)

        elif char in ")}]":
            if not stack or not is_matching(stack.pop(), char):
                return False

    # Ensure the stack is empty at the end, indicating balanced brackets
    return not stack and inp[-1] not in operators if inp else False


def is_matching(opening, closing):
    return (opening == '(' and closing == ')') or \
           (opening == '{' and closing == '}') or \
           (opening == '[' and closing == ']')


def main():
    history = History()
    
    while True:
        inp = input(">> ").strip()
    
        if inp == "":
            continue

        if inp == "quit" or inp == "exit":
            return 0

        valid = is_valid(inp)

        if valid:
            result = eval(inp)
            history.append_operation(inp, result)
            print(result)
            continue
        
        if not valid:
            print("Invalid Input!!")


def onquit():
    print("Quitting the Application...")
    print()
