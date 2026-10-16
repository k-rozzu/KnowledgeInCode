class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)

        if value <= node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)

        return node

    def print_tree(self):
        self._print_tree_recursive(self.root)

    def _print_tree_recursive(self, node):
        if node is not None:
            self._print_tree_recursive(node.left)
            print(node.value)
            self._print_tree_recursive(node.right)


arbol = BinaryTree()
arbol.insert(0)
arbol.insert(0)
arbol.insert(1)
arbol.insert(0)
arbol.insert(1)
arbol.insert(0)
arbol.insert(1)

arbol.print_tree()





