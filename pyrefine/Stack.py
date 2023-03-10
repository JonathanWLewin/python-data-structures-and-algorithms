class Stack():
    #Initialization of empty stack
    def __init__(self) -> None:
        super().__init__()
        self.stack = []
        
    #Check if stack is empty
    def empty(self):
        return len(self.stack) == 0
    
    #Check how many entries are in the stack
    def size(self):
        return len(self.stack)
    
    #Look at the entry on the top of the stack
    def top(self):
        return self.stack[-1]
    
    #Look at the entry on the top of the stack
    def peek(self):
        return self.top()
    
    #Push value to the top of the stack
    def push(self, val):
        self.stack.append(val)

    #Alias for top
    def pop(self):
        return self.stack.pop()