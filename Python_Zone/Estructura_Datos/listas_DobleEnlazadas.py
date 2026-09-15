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

    def print_forward(self):
        """Traverse and print the list from head to tail. """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "Empty list")

    def print_backward(self):
        """Traverse and print the list from tail to head. """
        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev
            print(" <-> ".join(elements) if elements else "Empty list")

# Ejemplo:
dll = DoublyLinkedList()
dll.append("Juan")
dll.append("Peter")
dll.append("Pepe")
dll.append("Jose")
dll.prepend("Maria")

print("\nForward Traverse: ")
dll.print_forward()
print("\nBackward Traverse: ")
dll.print_backward()
