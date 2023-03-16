import inspect

from pyrefine.Classes.DataStructureObject import DataStructureObject
from pyrefine.Classes.Example import Example
from pyrefine.Classes.Override import Override
from pyrefine.DataStructures.LinkedList import LinkedList


class LinkedListImplementor(DataStructureObject):

    _code_module = LinkedList
    _title = "Singly Linked List"
    _format_overrides = []
    _structure: LinkedList.LinkedList
    def __init__(self) -> None:
        super().__init__()

    def generate_examples(self):
        examples = []
        self._structure = LinkedList.LinkedList()
        examples.append(self.create_example_with_state('Initialization', 'Initialization of Linked List', 'lst = LinkedList()'))
        self._structure.add_end(1)
        examples.append(self.create_example_with_state('Initialization', 'Initialization of Linked List', 'lst = LinkedList()'))
        return examples