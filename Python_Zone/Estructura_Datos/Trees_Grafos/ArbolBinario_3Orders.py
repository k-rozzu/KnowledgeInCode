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

    def print_tree_relationships(self, node, relation="Raíz"):
        """Imprime la relación de cada nodo respecto a su padre."""
        if node is None:
            return

        print(f"{relation}: {node.value}")

        if node.left:
            self.print_tree_relationships(node.left, f"  Hijo Izquierdo de {node.value}")
        if node.right:
            self.print_tree_relationships(node.right, f"  Hijo Derecho de {node.value}")


# --- Creación de los nodos ---
n45 = Node(45)
n12 = Node(12)
n28 = Node(28)
n7 = Node(7)
n34 = Node(34)
n89 = Node(89)
n56 = Node(56)
n91 = Node(91)
n67 = Node(67)

# --- Construcción de las conexiones ---
arbol = BinaryTree()
arbol.root = n45

# Subárbol izquierdo de 45
n45.left = n12
n12.left = n28
n12.right = n7

# Subárbol derecho de 45
n45.right = n34
n34.left = n89
n34.right = n67

# Descendientes de 89
n89.left = n56
n89.right = n91

# --- Impresión de las relaciones ---
print("--- Descripción del Árbol ---")
arbol.print_tree_relationships(arbol.root)
print("\n" + "=" * 30 + "\n")

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