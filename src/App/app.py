import string

def welcome():
    print("WELCOME TO COMMANDLINE CALCULATOR!!")
    print()


def is_valid(inp):
    valid_char = set(string.digits + "+-*/%=><(). ")
    operators = set("+-*/%=<>")
    for i, char in enumerate(inp):
        if char not in valid_char:
            return False
        if i == 0 and char in operators:
            return False  # Disallow starting with an operator
        if i == len(inp) - 1 and char in operators:
            return False  # Disallow ending with an operator
    return True


def main():
    while True:
        inp = input(">> ").split()
    
        if inp == "":
            continue

        if inp == "quit" or inp == "exit":
            return 0

        valid = is_valid(inp)

        if valid:
            result = eval(inp)
            print(result)
            continue
        
        if not valid:
            print("Invalid Input!!")


def onquit():
    print("Quitting the Application...")
    print()
