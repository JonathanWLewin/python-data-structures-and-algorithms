from pyrefine.Classes import Example
from pyrefine.Classes.AlgorithmBaseObject import AlgorithmBaseObject
from pyrefine.Algorithms.AddTwoNumbers import AddTwoNumbers
import copy

class ListNode:
    # List node for linked list structure
    def __init__(self, id, val=0, next=None):
        self.val = val
        self.next = next
        self.id = id
        

class AddTwoNumbersImplementer(AlgorithmBaseObject):
    _title='Add Two Numbers'
    _code_module = AddTwoNumbers
    _examples = [
        {
            "input": {
                "L1":  [2,4,3], 
                "L2": [5,6,4]
            },
            "output": [7, 0, 8]
        },
        {
            "input": {
                "L1":  [0], 
                "L2": [0]
            },
            "output": [0]
        },
        {
            "input": {
                "L1":  [9, 9, 9, 9, 9, 9], 
                "L2": [9, 9, 9, 9]
            },
            "output": [8, 9, 9, 9, 0, 0, 1]
        }
    ]
    _methods = ["Enumerate"]
    _anchors = {}

    def __init__(self) -> None:
        super().__init__()

    def generate_example(self, example_number=None, custom_example_input=None, target=None, method=None):
        # Generate examples based on the example index passed in, or use the custom input and target passed in
        steps = []
        example = {}
        if example_number is not None:
            example = self._examples[example_number]
        elif custom_example_input is not None:
            example = {
                "input": custom_example_input
            }
        
        steps, output = self.addTwoNumbers(self.create_list(example["input"]["L1"]), self.create_list(example["input"]["L2"]), steps)
        example["steps"] = steps
        example["output"] = output
        return example
    
    def create_list(self, arr):
        '''
        Create a linked list from an array
        Include an id for reference in jinja template
        :param arr: list
        :return: ListNode
        '''
        BaseNode = ListNode(0, val=0)
        currNode = BaseNode
        for key, val in enumerate(arr):
            currNode.val = val
            currNode.id = key
            if key + 1 < len(arr):
                newNode = ListNode(key + 1, val = 0)
                currNode.next = newNode
                currNode = newNode
        return BaseNode


    def addTwoNumbers(self, l1, l2, steps):
        '''
        Pass in two linked list nodes and return a linked list with the sum of the two numbers
        :param l1: ListNode
        :param l2: ListNode
        :return: ListNode
        '''
        # Setup a carry value and a base node to return
        carry = 0
        currNode = ListNode(0)
        baseNode = ListNode(0, currNode)
        values_arr = []
        # Iterate through the linked lists and add the values together, until both are none and there is no carry
        while l1 is not None or l2 is not None or carry != 0:
            # Setup initial values for the two numbers, make sure that on None values we have 0
            oneVal = l1.val if l1 is not None else 0
            twoVal = l2.val if l2 is not None else 0

            # Add the two values together and the carry
            sum = oneVal + twoVal + carry
            # Get the digit from the modulo of the sum, and the carry from the floor division of the sum.
            digit = sum % 10
            carry = sum // 10
            # Curr node is going to be the digit and the next node is going to be a new node
            currNode.val = digit
            values_arr.append(digit)
            newNode = ListNode(0)
            # Only set the next node if there is a next node in the linked list or if there is a carry
            if (l1 is not None and l1.next is not None) or (l2 is not None and l2.next is not None) or carry != 0:
                currNode.next = newNode
                currNode = newNode

            steps.append({
                "values_to_display": {
                    "carry Value": carry
                },
                "L1": l1,
                "L2": l2,
                "values_arr": copy.deepcopy(values_arr)
            })

            # Iterate through the linked lists
            l1 = l1.next if l1 is not None and l1.next is not None else None
            l2 = l2.next if l2 is not None and l2.next is not None else None
        return steps, values_arr