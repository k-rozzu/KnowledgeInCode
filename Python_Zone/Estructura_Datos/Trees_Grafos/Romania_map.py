# Importar librerias para crear el grafo visualmente.
import networkx as nx
import matplotlib.pyplot as plt

# Crear los nodos (ciudades) del grafo.
# Tiene un valor = value (nombre de la ciudad).
# Tiene conexiones, pero como no sabemos cuántas, las guardamos = connections
class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

# Crear las aristas (carreteras).
# Tienen un inicio u origen = origin
# Tienen un destino o final = destination
# Tienen un peso o distancia en km = weight
class Edge:
    def __init__(self, origin, destination, weight):
        self.origin = origin
        self.destination = destination
        self.weight = weight

# Creamos 20 nodos (ciudades)
node_arad = Node('Arad')
node_zerind = Node('Zerind')
node_oradea = Node('Oradea')
node_timisoara = Node('Timisoara')
node_lugoj = Node('Lugoj')
node_mehadia = Node('Mehadia')
node_drobeta = Node('Drobeta')
node_craiova = Node('Craiova')
node_sibiu = Node('Sibiu')
node_rimnicu = Node('Rimnicu Vilcea')
node_fagaras = Node('Fagaras')
node_pitesti = Node('Pitesti')
node_bucharest = Node('Bucharest')
node_giurgiu = Node('Giurgiu')
node_urziceni = Node('Urziceni')
node_hirsova = Node('Hirsova')
node_eforie = Node('Eforie')
node_vaslui = Node('Vaslui')
node_iasi = Node('Iasi')
node_neamt = Node('Neamt')

# Definimos las aristas (node_origen, node_destino, distancia)
edge_arad_zerind = Edge(node_arad, node_zerind, 75)
edge_arad_sibiu = Edge(node_arad, node_sibiu, 140)
edge_arad_timisoara = Edge(node_arad, node_timisoara, 118)
edge_zerind_oradea = Edge(node_zerind, node_oradea, 71)
edge_oradea_sibiu = Edge(node_oradea, node_sibiu, 151)
edge_timisoara_lugoj = Edge(node_timisoara, node_lugoj, 111)
edge_lugoj_mehadia = Edge(node_lugoj, node_mehadia, 70)
edge_mehadia_drobeta = Edge(node_mehadia, node_drobeta, 75)
edge_drobeta_craiova = Edge(node_drobeta, node_craiova, 120)
edge_craiova_rimnicu = Edge(node_craiova, node_rimnicu, 146)
edge_craiova_pitesti = Edge(node_craiova, node_pitesti, 138)
edge_sibiu_fagaras = Edge(node_sibiu, node_fagaras, 99)
edge_sibiu_rimnicu = Edge(node_sibiu, node_rimnicu, 80)
edge_rimnicu_pitesti = Edge(node_rimnicu, node_pitesti, 97)
edge_fagaras_bucharest = Edge(node_fagaras, node_bucharest, 211)
edge_pitesti_bucharest = Edge(node_pitesti, node_bucharest, 101)
edge_bucharest_giurgiu = Edge(node_bucharest, node_giurgiu, 90)
edge_bucharest_urziceni = Edge(node_bucharest, node_urziceni, 85)
edge_urziceni_hirsova = Edge(node_urziceni, node_hirsova, 98)
edge_hirsova_eforie = Edge(node_hirsova, node_eforie, 86)
edge_urziceni_vaslui = Edge(node_urziceni, node_vaslui, 142)
edge_vaslui_iasi = Edge(node_vaslui, node_iasi, 92)
edge_iasi_neamt = Edge(node_iasi, node_neamt, 87)

# Guardamos todas las aristas en una lista para recorrerlas fácilmente
edges = [
    edge_arad_zerind, edge_arad_sibiu, edge_arad_timisoara,
    edge_zerind_oradea, edge_oradea_sibiu, edge_timisoara_lugoj,
    edge_lugoj_mehadia, edge_mehadia_drobeta, edge_drobeta_craiova,
    edge_craiova_rimnicu, edge_craiova_pitesti, edge_sibiu_fagaras,
    edge_sibiu_rimnicu, edge_rimnicu_pitesti, edge_fagaras_bucharest,
    edge_pitesti_bucharest, edge_bucharest_giurgiu, edge_bucharest_urziceni,
    edge_urziceni_hirsova, edge_hirsova_eforie, edge_urziceni_vaslui,
    edge_vaslui_iasi, edge_iasi_neamt,
]

# Las carreteras van en ambos sentidos, así que guardamos la conexión en los dos nodos
for edge in edges:
    edge.origin.connections.append(edge)
    edge.destination.connections.append(Edge(edge.destination, edge.origin, edge.weight))

# Crear un grafo no dirigido (las carreteras son de doble sentido)
G = nx.Graph()

# Agregar cada arista al grafo con su distancia como peso
for edge in edges:
    G.add_edge(edge.origin.value, edge.destination.value, weight=edge.weight)

# Posiciones exactas (x, y) de cada ciudad para que se vea como en el mapa
pos = {
    'Oradea': (126, -32),
    'Zerind': (94, -89),
    'Arad': (68, -146),
    'Timisoara': (72, -263),
    'Lugoj': (174, -308),
    'Mehadia': (180, -364),
    'Drobeta': (174, -421),
    'Craiova': (300, -438),
    'Sibiu': (236, -195),
    'Rimnicu Vilcea': (272, -263),
    'Fagaras': (377, -206),
    'Pitesti': (398, -325),
    'Bucharest': (512, -382),
    'Giurgiu': (476, -462),
    'Urziceni': (593, -349),
    'Hirsova': (704, -349),
    'Eforie': (743, -430),
    'Vaslui': (668, -214),
    'Iasi': (617, -124),
    'Neamt': (520, -79),
}

# Mostrar visualmente el grafo usando nuestras librerias
plt.figure(figsize=(12, 7))
nx.draw(G, pos, with_labels=True, node_shape='s', node_color='lightgray',
        edgecolors='black', node_size=300, font_size=9)

# Dibujar las distancias sobre cada arista
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

# Título del mapa y mostrar la ventana
plt.title('Mapa simplificado de Rumania')
plt.show()