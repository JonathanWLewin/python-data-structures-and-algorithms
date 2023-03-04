import inspect
from pyrefine.BaseObject import BaseObject
from pyrefine.Example import Example 
from pyrefine.Stack import Stack
from pyrefine.CodeFormatter import format_code

class StackImplementer(BaseObject):
    _description = "A stack implements FIFO"
    _code = inspect.getsource(Stack)
    _title = "Stack"
    def __init__(self) -> None:
        super().__init__()
    
    def generate_examples(self):
        code_string = """
        class Stack:
            def __init__():
                pass
            
        stack = Stack()"""
        examples = []
        stack = Stack()
        examples.append(Example('Initialization', 'Initialization of empty stack', 2, format_code(code_string), reversed(stack.stack)))
        stack.push(1)
        examples.append(Example('Push', 'Initialization of empty stack', 18, 'stack.push(1)', reversed(stack.stack)))
        stack.push(5)
        examples.append(Example('Push', 'Initialization of empty stack', 18, 'stack.push(5)', reversed(stack.stack)))
        return examples