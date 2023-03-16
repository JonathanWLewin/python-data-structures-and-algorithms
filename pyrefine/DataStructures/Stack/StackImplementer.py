import inspect

from pyrefine.Classes.DataStructureObject import DataStructureObject
from pyrefine.Classes.Example import Example
from pyrefine.Classes.Override import Override
from pyrefine.DataStructures.Stack import Stack


class StackImplementer(DataStructureObject):
    _code_module= Stack
    _title = "Stack"
    _structure: Stack.Stack
    def __init__(self) -> None:
        self._structure = Stack.Stack()
        super().__init__()
        self._format_overrides += [Override('append', 'func')]
    
    def generate_examples(self):
        examples = []
        examples.append(self.create_example_with_state('Initialization', 'Initialization of empty stack', 'stack = Stack()'))
        self._structure.push(1)
        examples.append(self.create_example_with_state('Push', 'Push to top of stack', 'stack.push(1)'))
        self._structure.push(5)
        examples.append(self.create_example_with_state('Push', 'Push to top of stack', 'stack.push(5)'))
        examples.append(self.create_example_with_state('Empty', 'Check if stack is empty', 'stack.empty()', self._structure.empty()))
        examples.append(self.create_example_with_state('Size', 'Check how many entries are in the stack', 'stack.size()', self._structure.size()))
        examples.append(self.create_example_with_state('Top', 'Look at the entry on the top of the stack', 'stack.top()', self._structure.top()))
        examples.append(self.create_example_with_state('Peek', 'Alias for top', 'stack.peek()', self._structure.peek()))
        examples.append(self.create_example_with_state('Pop', 'Removes top item and returns it', 'stack.pop()', self._structure.pop()))
        return examples