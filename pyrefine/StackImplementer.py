import inspect
from pyrefine.BaseObject import BaseObject
from pyrefine.Example import Example 
from pyrefine.Stack import Stack

class StackImplementer(BaseObject):
    _description = "A stack implements FIFO"
    _code = inspect.getsource(Stack)
    _title = "Stack"
    def __init__(self) -> None:
        super().__init__()
    
    def generate_examples(self):
        examples = [
            Example('Initialization', 'Initialization of empty stack', 2, 'stack = Stack()', reversed(self.example_1())),
            Example('Push', 'Pushing a value to the top of the stack', 18, 'stack.push(15)', reversed(self.example_2()))
        ]
        return examples
    
    def example_1(self):
        stack = Stack()
        return stack.stack
    
    def example_2(self):
        stack = Stack()
        stack.push(2)
        return stack.stack