class Stack():
    def __init__(self) -> None:
        super().__init__()
        self.stack = []

    def empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def top(self):
        return self.stack[-1]
    
    def peek(self):
        return self.top()
    
    def push(self, val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()