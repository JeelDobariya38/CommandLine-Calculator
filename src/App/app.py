import string

def welcome():
    print("WELCOME TO COMMANDLINE CALCULATOR!!")
    print()


def is_valid(inp):
    valid_char = set(string.digits + "+-*/%=>< ")
    return all(char in valid_char for char in inp)


def main():
    while True:
        inp = input(">> ").split()
    
        if inp == "":
            continue

        if inp == "quit" or inp == "exit":
            return 0

        valid = isvalid(inp)

        if valid:
            result = eval(inp)
            print(result)
            continue
        
        if not valid:
            print("Invalid Input!!")


def onquit():
    print("Quitting the Application...")
    print()
