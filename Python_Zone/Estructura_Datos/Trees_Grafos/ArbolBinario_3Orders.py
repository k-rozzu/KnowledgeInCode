class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, node):
        if node is not None:
            self.inorderTraversal(node.left)
            print(node.value, end=" ")
            self.inorderTraversal(node.right)

    def preorderTraversal(self, node):
        if node is not None:
            print(node.value, end=" ")
            self.preorderTraversal(node.left)
            self.preorderTraversal(node.right)

    def postorderTraversal(self, node):
        if node is not None:
            self.postorderTraversal(node.left)
            self.postorderTraversal(node.right)
            print(node.value, end=" ")

# --- Creación de los nodos ---
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)

# --- Construcción explícita de las conexiones ---
arbol = BinaryTree()
arbol.root = n1

# Subárbol izquierdo de 1
n1.left = n2
n2.left = n3
n2.right = n4
n4.left = n5

# Subárbol derecho de 1
n1.right = n6
n6.left = n7
n6.right = n9
n7.left = n8

# --- Comprobación de recorridos ---
print("Preorder Traversal: ")
arbol.preorderTraversal(arbol.root)
print("\n")

print("Inorder Traversal: ")
arbol.inorderTraversal(arbol.root)
print("\n")

print("Postorder Traversal: ")
arbol.postorderTraversal(arbol.root)
print("\n")