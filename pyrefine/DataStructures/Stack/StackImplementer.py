import inspect

from pyrefine.Classes.DataStructureObject import DataStructureObject
from pyrefine.Classes.Example import Example
from pyrefine.Classes.Override import Override
from pyrefine.DataStructures.Stack.Stack import Stack
from pyrefine.Helpers.CodeFormatter import format_code


class StackImplementer(DataStructureObject):
    _code = inspect.getsource(Stack)
    _title = "Stack"
    _format_overrides = [
        Override('empty', 'func'),
        Override('size', 'func'),
        Override('top', 'func'),
        Override('peek', 'func'),
        Override('push', 'func'),
        Override('pop', 'func'),
        Override('Stack', 'class'),
        Override('append', 'func'),
    ]
    _stack: Stack
    def __init__(self) -> None:
        super().__init__()
    
    def generate_examples(self):
        examples = []
        self._stack = Stack()
        examples.append(self.create_example_with_state('Initialization', 'Initialization of empty stack', 'stack = Stack()'))
        self._stack.push(1)
        examples.append(self.create_example_with_state('Push', 'Push to top of stack', 'stack.push(1)'))
        self._stack.push(5)
        examples.append(self.create_example_with_state('Push', 'Push to top of stack', 'stack.push(5)'))
        examples.append(self.create_example_with_state('Empty', 'Check if stack is empty', 'stack.empty()', self._stack.empty()))
        examples.append(self.create_example_with_state('Size', 'Check how many entries are in the stack', 'stack.size()', self._stack.size()))
        examples.append(self.create_example_with_state('Top', 'Look at the entry on the top of the stack', 'stack.top()', self._stack.top()))
        examples.append(self.create_example_with_state('Peek', 'Alias for top', 'stack.peek()', self._stack.peek()))
        examples.append(self.create_example_with_state('Pop', 'Removes top item and returns it', 'stack.pop()', self._stack.pop()))
        return examples
    
    def create_example_with_state(self, title, description, input, output=''):
        return Example(title, description, input, output, [x for x in reversed(self._stack.stack)])