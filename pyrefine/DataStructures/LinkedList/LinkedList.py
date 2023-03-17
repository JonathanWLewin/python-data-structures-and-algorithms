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
            curr = curr.nxt
        return "->".join(map(str, lst))
    
    def __iter__(self):
        """
        Returns an iterator of the linked list
        O(n)
        """
        if self.head is not None:
            curr = self.head
            while curr:
                yield curr.val
                curr = curr.nxt

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
        node.nxt = self.head
        self.head = node
        self._size += 1

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
            while curr.nxt is not None:
                curr = curr.nxt
            curr.nxt = node
        self._size += 1

    def remove_front(self):
        """
        Remove first node in a linked list
        Time Complexity O(1)
        """
        if self.head is None:
            return None
        else:
            temp = self.head
            self.head = self.head.nxt
            temp.nxt = None
            self._size -= 1
            return temp.val
        
    def remove_end(self):
        """
        Remove last node in a linked list
        Time Complexity O(n)
        """
        if self.head is None:
            return None
        elif self.head.nxt is None:
            temp = self.head
            self.head = None
            self._size -= 1
            return temp.val
        else:
            curr = self.head
            while curr.nxt.nxt is not None:
                curr = curr.nxt
            temp = curr.nxt
            curr.nxt = None
            self._size -= 1
            return temp.val
        
    def insert_at_index(self, val, index):
        """
        Insert node at index
        Time Complexity O(n)
        """
        if self.size < index or index < 0:
            raise IndexError('Index provided larger than the size of the list')
        if index == 0:
            self.add_front(val)
        if index == self.size:
            self.add_end(val)
        else:
            node = Node(val)
            curr = self.head
            for i in range(index):
                curr = curr.nxt
            node.nxt = curr.nxt
            curr.nxt = node
            self.size += 1
        
    def remove_at_index(self, index):
        """
        Remove node at index
        Time Complexity O(n)
        """
        if self.size < index or index < 0:
            raise IndexError('Index provided larger than the size of the list')
        elif index == 0:
            self.remove_front()
        elif index == self.size - 1:
            self.remove_end()
        else:
            curr = self.head
            for i in range(index - 1):
                curr = curr.nxt
            curr.nxt = curr.nxt.nxt
            self.size =- 1
            
    def get_val_at_index(self, index):
        """
        Get the value from a node at a specific index
        Time Complexity O(n)
        """
        if self.size < index or index < 0:
            raise IndexError('Index provided larger than the size of the list')
        elif index == 0:
            return self.head.val
        else:
            curr = self.head
            for i in range(index):
                curr = curr.nxt
            return curr.val
        
    def find_val_in_list(self, val):
        """
        Find the first node with the given value and return the index, return -1 if not found
        Time Complexity O(n)
        """
        curr = self.head
        i = 0
        while curr.nxt is not None:
            if curr.val == val:
                return i
            curr = curr.nxt
            i += 1
        return -1