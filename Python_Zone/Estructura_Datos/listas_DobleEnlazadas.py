# Double linked list

class Node:
    """ Represents a single node in the list. """

    def __init__(self, data):
        self.data = data
        self.next = None # pointer to next node
        self.prev = None # pointer to the previous node

class DoublyLinkedList:
    """ Manages the nodes and bidirectional links. """

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        """Inserts a new node at the beginning (head)"""

        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, data):
        """Inserts a new node at the end (tail)"""

        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
            return

        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node