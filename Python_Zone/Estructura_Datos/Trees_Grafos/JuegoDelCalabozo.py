# Clase que representa cada habitación (nodo) del grafo
class Node:
    def __init__(self, posicion):
        self.posicion = posicion  # Coordenadas (fila, columna)
        self.vecinos = []  # Lista de nodos adyacentes (conexiones en cruz)


# Construcción del mapa de 4x4 usando la clase Node
nodos = {(r, c): Node((r, c)) for r in range(1, 5) for c in range(1, 5)}

# Conexión de los nodos en cruz
for (r, c), nodo in nodos.items():
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        vecino_pos = (r + dr, c + dc)
        if vecino_pos in nodos:
            nodo.vecinos.append(nodos[vecino_pos])

# Posiciones de los elementos según el mapa
pozos = [(1, 3), (3, 3), (4, 4)]
monstruo = (3, 1)
oro = (3, 2)


# Función para verificar brisas o hedores en casillas adyacentes
def verificar_caracteristicas(nodo_actual):
    r, c = nodo_actual.posicion

    # Comprueba si hay un monstruo en alguna habitación vecina
    if any(v.posicion == monstruo for v in nodo_actual.vecinos):
        print(f"Habitación [{r},{c}]: Hedor detectado ¡Cuidado, puedes estar cerca del monstruo!")

    # Comprueba si hay un pozo en alguna habitación vecina
    if any(v.posicion in pozos for v in nodo_actual.vecinos):
        print(f"Habitación [{r},{c}]: Brisa detectada ¡Cuidado, puedes estar cerca de un pozo!")


# Función principal del flujo del juego
def jugar():
    nodo_actual = nodos[(1, 1)]
    print("--- ¡Bienvenido al juego de la cueva! ---\n")
    print("Inicio en la habitación [1,1]")

    while True:
        pos = nodo_actual.posicion

        # Validación de pozos
        if pos in pozos:
            print(f"Habitación [{pos[0]},{pos[1]}]: Has caído en un pozo y te estrellaste en el fondo, moriste.")
            reiniciar = input("¿Volver a jugar? (si/no): ").strip().lower()
            if reiniciar == 'si':
                nodo_actual = nodos[(1, 1)]
                print("\nReiniciando en la casilla de inicio [1,1]...\n")
                continue
            else:
                print("¡Gracias por jugar!")
                break

        # Validación del monstruo
        if pos == monstruo:
            print(f"Habitación [{pos[0]},{pos[1]}]: El monstruo te ha destripado, moriste.")
            reiniciar = input("¿Volver a jugar? (si/no): ").strip().lower()
            if reiniciar == 'si':
                nodo_actual = nodos[(1, 1)]
                print("\nReiniciando en la casilla de inicio [1,1]...\n")
                continue
            else:
                print("¡Gracias por jugar!")
                break

        # Validación del oro
        if pos == oro:
            print(f"Habitación [{pos[0]},{pos[1]}]: ¡Felicidades! ¡Has encontrado el oro!")
            break

        # Imprime avisos cercanos
        verificar_caracteristicas(nodo_actual)

        # Muestra vecinos disponibles e interactúa con el usuario
        vecinos_pos = [v.posicion for v in nodo_actual.vecinos]
        print(f"\nTe encuentras en {list(pos)}. Vecinos accesibles: {[list(v) for v in vecinos_pos]}")

        # Recibe la coordenada completa en una sola línea (ejemplo: 1, 2)
        entrada = input("Ingresa la habitación a moverte (ejemplo: 1, 2): ")
        try:
            partes = entrada.split(',')
            f = int(partes[0].strip())
            c = int(partes[1].strip())
            destino_pos = (f, c)

            # Busca si la posición elegida corresponde a un nodo vecino
            siguiente_nodo = next((v for v in nodo_actual.vecinos if v.posicion == destino_pos), None)

            if siguiente_nodo:
                nodo_actual = siguiente_nodo
            else:
                print(">> Movimiento inválido. Solo puedes moverte a habitaciones adyacentes en cruz.\n")
        except Exception:
            print(">> Entrada no válida. Usa el formato 'fila, columna' (ejemplo: 1, 2).\n")


# Inicia la ejecución
jugar()