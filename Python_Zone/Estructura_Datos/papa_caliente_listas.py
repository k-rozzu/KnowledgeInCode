import random

class Node:
    """
    Representa a cada jugador.
    Guarda el nombre (data) y la referencia al siguiente nodo (next).
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class ListaCircular:
    """
    Estructura encargada de gestionar el círculo de nodos.
    """

    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Inserta un nuevo jugador al final y asegura que la lista siga siendo circular.
        """
        new_node = Node(data)

        # Si el círculo está vacío, el nuevo nodo se apunta a sí mismo
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return

        # Buscamos el último nodo (el que apunta de vuelta a head)
        currentNode = self.head
        while currentNode.next != self.head:
            currentNode = currentNode.next

        # Enlazamos el nuevo nodo para cerrar el círculo
        currentNode.next = new_node
        new_node.next = self.head

    def play(self):
        """
        Recorre la lista circular y elimina nodos usando un número aleatorio de pases.
        """
        currentNode = self.head

        # El juego continúa mientras haya más de un jugador (currentNode.next != currentNode)
        while currentNode.next != currentNode:
            # Número aleatorio de pases para la patata caliente
            pases = random.randint(1, 5)

            # Avanzamos los pases (paramos en el nodo previo al eliminado)
            for _ in range(pases - 1):
                currentNode = currentNode.next

            # Identificamos y eliminamos al perdedor
            eliminado = currentNode.next
            print(f"Pases: {pases} -> Eliminado: {eliminado.data}")

            # Reenlazamos los punteros saltando al nodo eliminado
            currentNode.next = eliminado.next

            # Continuamos el juego desde el siguiente jugador
            currentNode = currentNode.next

            # --- IMPRIMIR JUGADORES RESTANTES ---
            temp = currentNode
            quedan = []

            while True:
                quedan.append(temp.data)
                temp = temp.next
                if temp == currentNode:
                    break

            print(f"\nQuedan ({len(quedan)}): {' -> '.join(quedan)}")

        # Cuando solo queda un nodo apuntándose a sí mismo
        print(f"\n¡El ganador es {currentNode.data}!")


círculo = ListaCircular()

# Agregamos los participantes usando append
círculo.append("Carolina")
círculo.append("Dana")
círculo.append("Alan")
círculo.append("Miranda")
círculo.append("Diego")

# Iniciamos el recorrido/juego
círculo.play()

