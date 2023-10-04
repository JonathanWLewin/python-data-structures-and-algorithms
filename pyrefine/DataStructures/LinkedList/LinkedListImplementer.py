import inspect

from pyrefine.Classes.DataStructureObject import DataStructureObject
from pyrefine.Classes.Example import Example
from pyrefine.Classes.Override import Override
from pyrefine.DataStructures.LinkedList import LinkedList


class LinkedListImplementer(DataStructureObject):

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
        examples.append(self.create_example_with_state('Empty', 'Check if the list is empty', 'self._structure.is_empty', self._structure.is_empty))
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
        examples.append(self.create_example_with_state('Empty', 'Check if the list is empty', 'self._structure.is_empty', self._structure.is_empty))
        self._structure.add_end(20)
        examples.append(self.create_example_with_state('Add to end', 'Add value to the front of the linked list', 'lst.add_end(20)'))
        self._structure.remove_end()
        examples.append(self.create_example_with_state('Remove from end', 'Remove value from the end of the linked list', 'lst.remove_end()'))
        self._structure.remove_front()
        examples.append(self.create_example_with_state('Remove from front', 'Remove value from the front of the linked list', 'lst.remove_front()'))
        examples.append(self.create_example_with_state('Size', 'Return the number of nodes in the list', 'lst.size', self._structure.size))
        self._structure.insert_at_index(45, 4)
        examples.append(self.create_example_with_state('Insert At Index', 'Inserts node at a specific index of the list', 'lst.insert_at_index(45, 4)'))
        self._structure.remove_at_index(4)
        examples.append(self.create_example_with_state('Remove At Index', 'Removes node at a specific index of the list', 'lst.remove_at_index(4)'))
        examples.append(self.create_example_with_state('Get Val At Index', 'Gets the value of a node at a specific index of the list', 'lst.get_val_at_index(4)', self._structure.get_val_at_index(4)))
        examples.append(self.create_example_with_state('Find Val In List', 'Gets the index of a value in the list', 'lst.find_val_in_list(8)', self._structure.find_val_in_list(8)))
        examples.append(self.create_example_with_state('Find Val In List', 'Search for value that does not exist returns -1', 'lst.find_val_in_list(10000)', self._structure.find_val_in_list(10000)))
        return examples