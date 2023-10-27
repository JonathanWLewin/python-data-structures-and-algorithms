class ListNode:
    # List node for linked list structure
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(self, l1, l2):
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
        newNode = ListNode(0)
        # Only set the next node if there is a next node in the linked list or if there is a carry
        if (l1 is not None and l1.next is not None) or (l2 is not None and l2.next is not None) or carry != 0:
            currNode.next = newNode
            currNode = newNode

        # Iterate through the linked lists
        l1 = l1.next if l1 is not None and l1.next is not None else None
        l2 = l2.next if l2 is not None and l2.next is not None else None
    return baseNode.next