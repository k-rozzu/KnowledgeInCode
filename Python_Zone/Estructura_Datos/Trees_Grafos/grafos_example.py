# importar librerias para crear el grafo visualmente.
import networkx as nx
import matplotlib.pyplot as plt

# Crear los nodos (vertices) del grafo.
# Puede tener valor = value.
# Puede tener conexiones, pero como no sabemos cuántas, las guardamos = connections
class Node:
    def __init__(self, value):
        self.value = value
        self.connections = []

# Crear las aristas/bordes.
# Tienen un inicio u origen = origin
# Tienen un destino o final = destination
class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

# Creamos 6 nodos (vertices)
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

# Definimos las aristas origen y destino (node_origen, node_destino)
edge_ab = Edge(node_a, node_b)
edge_bd = Edge(node_b, node_d)
edge_ac = Edge(node_a, node_c)
edge_cd = Edge(node_c, node_d)
edge_cf = Edge(node_c, node_f)
edge_de = Edge(node_d, node_e)
edge_ef = Edge(node_e, node_f)
edge_fd = Edge(node_f, node_d)
edge_fb = Edge(node_f, node_b)

# Guardamos las conexiones de cada nodo en su perspectivo arreglo (de node_x a => node_y)
node_a.connections.append(edge_ab)
node_a.connections.append(edge_ac)
node_b.connections.append(edge_bd)
node_c.connections.append(edge_cd)
node_c.connections.append(edge_cf)
node_d.connections.append(edge_de)
node_e.connections.append(edge_ef)
node_f.connections.append(edge_fd)
node_f.connections.append(edge_fb)

# Mostrar visualmente el grafo usando nuestras librerias
DG = nx.DiGraph()
DG.add_edges_from([(node_c.value, node_f.value),])
DG.add_edges_from([(node_c.value, node_d.value),])
DG.add_edges_from([(node_b.value, node_d.value),])
DG.add_edges_from([(node_a.value, node_b.value),])
DG.add_edges_from([(node_a.value, node_c.value),])
DG.add_edges_from([(node_d.value, node_e.value),])
DG.add_edges_from([(node_f.value, node_b.value),])
DG.add_edges_from([(node_f.value, node_d.value),])
DG.add_edges_from([(node_e.value, node_f.value),])
nx.draw(DG, with_labels=True)
plt.show()