class History:
    def __init__(self):
        self.history = []

    def append_operation(self, expression: str, result: str):
        self.history.append(expression + " -> " + result)
    
    def __repr__(self):
        string = ""
        for item in self.history:
            string += item + "\n"
        return string

    def clear_history(self):
        self.history = []
