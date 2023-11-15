class History:
    def __init__(self):
        self.history = []

    def append_operation(self, expression: str):
        self.history.append(expression)
    
    def print_history(self):
        for item in self.history:
            print(item)
        print()

    def clear_history(self):
        self.history = []
