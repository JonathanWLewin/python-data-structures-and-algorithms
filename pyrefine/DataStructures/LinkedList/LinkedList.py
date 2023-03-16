class Node():
    def __init__(self, val, nxt=None) -> None:
        """
        Initialization of Node
        Time Complexity O(1)
        """
        self.val = val
        self.nxt = nxt

class LinkedList():
    def __init__(self) -> None:
        """
        Initialization of a linked list
        Time Complexity O(1)
        """
        self.head = None
        self._size = 0

    def __str__(self) -> str:
        """
        Returns a string representation of the linked list
        O(n)
        """
        curr = self.head
        lst = []
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return "->".join(map(str, lst))
    
    def __iter__(self):
        """
        Returns an iterator of the linked list
        O(n)
        """
        curr = self.head
        while curr:
            yield curr.val
            curr = curr.next

    @property
    def size(self):
        """
        Getter funciton for size
        Time Complexity O(n)
        """
        return self._size
    
    @property
    def is_empty(self):
        """
        Getter function to check if linked list is empty
        Time Complexity O(1)
        """
        return self.head is None

    def add_front(self, val):
        """
        Add a node to the front of the linked list
        Time Complexity O(1)
        """
        node = Node(val)
        node.next = self.head
        self.head = node
        self.size += 1

    def add_end(self, val):
        """
        Add a node to the end of the linked list
        Time complexity O(n)
        """
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node
        self.size += 1

    def remove_front(self):
        """
        Remove first node in a linked list
        Time Complexity O(1)
        """
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.size -= 1
            return temp.val
        
    def remove_end(self):
        """
        Remove last node in a linked list
        Time Complexity O(n)
        """
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            self.size -= 1
            return temp.val
        else:
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            temp = curr.next
            curr.next = None
            self.size -= 1
            return temp.val