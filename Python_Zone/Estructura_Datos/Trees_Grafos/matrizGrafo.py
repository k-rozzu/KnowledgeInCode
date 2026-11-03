import string
import matplotlib.pyplot as plt
import networkx as nx


# Clase para representar un nodo con etiqueta y color asignado
class Node:

    def __init__(self, name, color):
        self.name = name
        self.color = color


# Solicitar el número de vértices para la matriz cuadrada N x N
num_nodes = int(input("Ingrese el número de vértices: "))

# Generar letras (A, B, C...) y una paleta de colores fija para los nodos
labels = list(string.ascii_uppercase[:num_nodes])
palette = [
    "skyblue",
    "lightcoral",
    "lightgreen",
    "gold",
    "plum",
    "orange",
    "cyan",
]
node_colors = [palette[i % len(palette)] for i in range(num_nodes)]

# Crear la lista de objetos Node asociándoles su color
nodes = [Node(labels[i], node_colors[i]) for i in range(num_nodes)]

# Inicializar la matriz de adyacencia vacía
adjacency_matrix = []

# Capturar los valores de la matriz indicando si hay dirección
print("\n--- Captura de la Matriz de Adyacencia Dirigida ---")
for i in range(num_nodes):
    row = []
    for j in range(num_nodes):
        val = int(input(f"Elemento [{labels[i]},{labels[j]}]: "))
        row.append(val)
    adjacency_matrix.append(row)

# Crear un grafo DIRIGIDO con NetworkX
G = nx.DiGraph()

# Agregar todos los nodos creados al grafo
for node in nodes:
    G.add_node(node.name, color=node.color)

# Conectar nodos y asignar a la arista el color del nodo de origen
for i in range(num_nodes):
    for j in range(num_nodes):
        if adjacency_matrix[i][j] == 1:
            G.add_edge(nodes[i].name, nodes[j].name, color=nodes[i].color)

# Calcular posiciones equilibradas usando un layout por resortes
pos = nx.spring_layout(G, k=1.2, seed=42)

# Extraer colores de los nodos y de las aristas en el orden del grafo
colors_of_nodes = [G.nodes[n]["color"] for n in G.nodes()]
colors_of_edges = [G.edges[e]["color"] for e in G.edges()]

# Dibujar los nodos con sus colores distintivos
nx.draw_networkx_nodes(
    G, pos, node_color=colors_of_nodes, node_size=2000, edgecolors="black"
)

# Dibujar las etiquetas de los nodos
nx.draw_networkx_labels(G, pos, font_size=12, font_weight="bold")

# Dibujar aristas curvadas con flechas y el color del nodo de origen
nx.draw_networkx_edges(
    G,
    pos,
    edge_color=colors_of_edges,
    arrows=True,
    arrowsize=20,
    connectionstyle="arc3,rad=0.2",
    width=2,
)

# Mostrar la ventana gráfica del grafo dirigido
plt.show()