class Stack():
    """
    A stack object implements Last In First Out (LIFO) or First In Last Out (FILO).
    """
    def __init__(self) -> None:
        """
        Initialization of empty stack
        Time Complexity O(1)
        """
        super().__init__()
        self.stack = []
        
    def empty(self):
        """
        Check if stack is empty
        Time Complexity O(1)
        """
        return len(self.stack) == 0
    
    def size(self):
        """
        Check how many entries are in the stack
        Time Complexity O(1)
        """
        return len(self.stack)
    
    def top(self):
        """
        Look at the entry on the top of the stack
        Time Complexity O(1)
        """
        return self.stack[-1]
    
    
    def peek(self):
        """
        Look at the entry on the top of the stack
        Time Complexity O(1)
        """
        return self.top()
    
    def push(self, val):
        """
        Push value to the top of the stack
        Time Complexity O(1)
        """
        self.stack.append(val)

    def pop(self):
        """
        Alias for top
        Time Complexity O(1)
        """
        return self.stack.pop()