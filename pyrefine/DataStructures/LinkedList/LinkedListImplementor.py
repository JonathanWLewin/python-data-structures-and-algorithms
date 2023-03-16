import inspect

from pyrefine.Classes.DataStructureObject import DataStructureObject
from pyrefine.Classes.Example import Example
from pyrefine.Classes.Override import Override
from pyrefine.DataStructures.LinkedList import LinkedList


class LinkedListImplementor(DataStructureObject):

    _code = inspect.getsource(LinkedList)
    _title = "Singly Linked List"
    _format_overrides = []
    _lst: LinkedList.LinkedList
    def __init__(self) -> None:
        super().__init__()
        for cls in inspect.getmembers(LinkedList, inspect.isclass):
            print(inspect.getmembers(cls[1], inspect.isfunction))

    def generate_examples(self):
        examples = []
        self._lst = LinkedList.LinkedList()
        examples.append(self.generate_example_with_state('Initialization', 'Initialization of Linked List', 'lst = LinkedList()'))
        return examples
    
    def generate_example_with_state(self, title, description, input, output='') -> Example:
        return Example(title, description, input, output, list(self._lst))