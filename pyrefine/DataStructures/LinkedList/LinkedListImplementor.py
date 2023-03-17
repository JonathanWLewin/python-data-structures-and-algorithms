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
        self._structure.add_front(1)
        examples.append(self.create_example_with_state('Add to front', 'Add value to the front of the linked list', 'lst.add_front(1)'))
        self._structure.add_front(3)
        examples.append(self.create_example_with_state('Add to front', 'Add value to the front of the linked list', 'lst.add_front(3)'))
        self._structure.add_front(4)
        examples.append(self.create_example_with_state('Add to front', 'Add value to the front of the linked list', 'lst.add_front(4)'))
        self._structure.add_front(6)
        self._structure.add_front(8)
        self._structure.add_front(15)
        self._structure.add_front(35)
        add_front_str = """self._structure.add_front(6)
self._structure.add_front(8)
self._structure.add_front(15)
self._structure.add_front(35)"""
        examples.append(self.create_example_with_state('Add to front', 'Add value to the front of the linked list', add_front_str))
        return examples