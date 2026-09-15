class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node("A")
node2 = Node("B")
node3 = Node("C")
node4 = Node("D")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node1

currentNode = node1
startNode = node1
print(currentNode.data, end= " -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end= " -> ")
    currentNode = currentNode.next

print("...")