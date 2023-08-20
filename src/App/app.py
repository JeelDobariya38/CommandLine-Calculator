def welcome():
    print("WELCOME TO COMMANDLINE CALCULATOR!!")
    print()

def isvalid(x):
    valid = True
    return valid

def main():
    while True:
        x = input(">> ")
        
        if x == "":
            continue

        if x == "quit" or x == "exit":
            return 0
        
        if isvalid(x):
            print(eval(x))

def onquit():
    print("Quitting the Application...")
    print()