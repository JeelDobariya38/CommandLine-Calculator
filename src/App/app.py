import string

def welcome():
    print("WELCOME TO COMMANDLINE CALCULATOR!!")
    print()


def isvalid(inp):
    number = list(string.digits)
    operator = "+ - * / % = > <".split(" ")
    valid_char = number + operator + [" "]
    for char in inp:
        if char not in valid_char:
            return False
    else:
        return True


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
