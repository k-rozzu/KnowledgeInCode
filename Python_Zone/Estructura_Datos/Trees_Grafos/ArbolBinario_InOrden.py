class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryCombinationTree:
    def __init__(self, depth, inorder_values):
        # 1. Construye el esqueleto del árbol con la profundidad deseada
        self.root = self._build_empty_tree(depth)

        # 2. Inserta los valores siguiendo el recorrido Inorden
        self._iter_values = iter(inorder_values)
        self._insert_inorder(self.root)

    def _build_empty_tree(self, depth):
        if depth == 0:
            return None

        node = Node()
        if depth > 1:
            node.left = self._build_empty_tree(depth - 1)
            node.right = self._build_empty_tree(depth - 1)

        return node

    def _insert_inorder(self, node):
        """Asigna valores a los nodos en orden: Izquierda -> Raíz -> Derecha"""
        if node is not None:
            self._insert_inorder(node.left)
            node.value = next(self._iter_values, None)
            self._insert_inorder(node.right)

    def print_inorder(self, node):
        """Recorre e imprime el árbol en Inorden"""
        if node is not None:
            self.print_inorder(node.left)
            print(node.value, end=" ")
            self.print_inorder(node.right)

    def print_visual(self, node, prefix="", is_left=True):
        """Imprime el árbol de forma gráfica en la consola"""
        if node is not None:
            print(prefix + ("├── " if is_left else "└── ") + str(node.value))
            child_prefix = prefix + ("│   " if is_left else "    ")
            self.print_visual(node.left, child_prefix, True)
            self.print_visual(node.right, child_prefix, False)

    def print_paths(self, node, path=None):
        """Imprime todas las rutas desde la raíz hasta las hojas"""
        if node is None:
            return

        if path is None:
            path = []

        # Usamos una lista para manejar números de más de un dígito correctamente
        current_path = path + [str(node.value)]

        if node.left is None and node.right is None:
            print("->".join(current_path))
        else:
            self.print_paths(node.left, current_path)
            self.print_paths(node.right, current_path)


# Valores extraídos de la imagen en recorrido Inorden
valores_inorden = [22, 3, 20, 15, 16, 10, 56, 26, 2, 99, 13, 5, 78, 45, 93]

# El árbol de la imagen tiene 4 niveles de profundidad
arbol = BinaryCombinationTree(depth=4, inorder_values=valores_inorden)

print("Estructura visual del árbol:")
arbol.print_visual(arbol.root)

print("\nRecorrido Inorden (Izquierda - Raíz - Derecha):")
arbol.print_inorder(arbol.root)
print()

print("\nRutas desde la raíz hasta las hojas:")
arbol.print_paths(arbol.root)