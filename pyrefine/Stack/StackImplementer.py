import inspect
from BaseObject import BaseObject
from Example import Example
from Stack import Stack
class StackImplementer(BaseObject):
    _description = "A stack implements FIFO"
    _code = inspect(Stack)
    _title = "Stack"
    def __init__(self) -> None:
        super().__init__()
        self.stack = Stack()
    
    def generate_examples(self):
        examples = [
            Example('Initialization', 'Initialization of empty stack', 2)
        ]
        return examples