import math
import matplotlib.pyplot as plt
import networkx as nx


class Node:

  def __init__(self, value):
    self.value = value
    self.connections = []


class Edge:

  def __init__(self, origin, destination, weight):
    self.origin = origin
    self.destination = destination
    self.weight = weight


# 1. CREACIÓN DE NODOS (CIUDADES)
node_a = Node("Neamt")
node_b = Node("Iasi")
node_c = Node("Vaslui")
node_d = Node("Urziceni")
node_e = Node("Hirsova")
node_f = Node("Eforie")
node_g = Node("Bucharest")
node_h = Node("Giurgiu")
node_i = Node("Fagaras")
node_j = Node("Pitesti")
node_k = Node("Sibiu")
node_l = Node("Rimnicu Vilcea")
node_m = Node("Craiova")
node_n = Node("Drobeta")
node_o = Node("Mehadia")
node_p = Node("Lugoj")
node_q = Node("Timisoara")
node_r = Node("Arad")
node_s = Node("Zerind")
node_t = Node("Oradea")

# 2. CREACIÓN DE CONEXIONES (ARISTAS / RUTAS)
edge_ab = Edge(node_a, node_b, 87)
edge_bc = Edge(node_b, node_c, 92)
edge_cd = Edge(node_c, node_d, 142)
edge_de = Edge(node_d, node_e, 98)
edge_ef = Edge(node_e, node_f, 86)
edge_dg = Edge(node_d, node_g, 85)
edge_gh = Edge(node_g, node_h, 90)
edge_gi = Edge(node_g, node_i, 211)
edge_gj = Edge(node_g, node_j, 101)
edge_ik = Edge(node_i, node_k, 99)
edge_jl = Edge(node_j, node_l, 97)
edge_jm = Edge(node_j, node_m, 138)
edge_lk = Edge(node_l, node_k, 80)
edge_ml = Edge(node_m, node_l, 146)
edge_kt = Edge(node_k, node_t, 151)
edge_ts = Edge(node_t, node_s, 71)
edge_sr = Edge(node_s, node_r, 75)
edge_rk = Edge(node_r, node_k, 140)
edge_rq = Edge(node_r, node_q, 118)
edge_qp = Edge(node_q, node_p, 111)
edge_po = Edge(node_p, node_o, 70)
edge_on = Edge(node_o, node_n, 75)
enge_nm = Edge(node_n, node_m, 120)

# Asignar conexiones de ida a los nodos
node_a.connections.append(edge_ab)
node_b.connections.append(edge_bc)
node_c.connections.append(edge_cd)
node_d.connections.append(edge_de)
node_d.connections.append(edge_dg)
node_e.connections.append(edge_ef)
node_g.connections.append(edge_gh)
node_g.connections.append(edge_gi)
node_g.connections.append(edge_gj)
node_i.connections.append(edge_ik)
node_j.connections.append(edge_jl)
node_j.connections.append(edge_jm)
node_l.connections.append(edge_lk)
node_m.connections.append(edge_ml)
node_k.connections.append(edge_kt)
node_t.connections.append(edge_ts)
node_s.connections.append(edge_sr)
node_r.connections.append(edge_rk)
node_r.connections.append(edge_rq)
node_q.connections.append(edge_qp)
node_p.connections.append(edge_po)
node_o.connections.append(edge_on)
node_n.connections.append(enge_nm)

# Como las carreteras son de doble sentido, agregamos las conexiones inversas
all_edges = [
    edge_ab,
    edge_bc,
    edge_cd,
    edge_de,
    edge_ef,
    edge_dg,
    edge_gh,
    edge_gi,
    edge_gj,
    edge_ik,
    edge_jl,
    edge_jm,
    edge_lk,
    edge_ml,
    edge_kt,
    edge_ts,
    edge_sr,
    edge_rk,
    edge_rq,
    edge_qp,
    edge_po,
    edge_on,
    enge_nm,
]
for edge in all_edges:
  # Agrega la arista invertida al nodo de destino
  edge.destination.connections.append(
      Edge(edge.destination, edge.origin, edge.weight)
  )

all_nodes = [
    node_a,
    node_b,
    node_c,
    node_d,
    node_e,
    node_f,
    node_g,
    node_h,
    node_i,
    node_j,
    node_k,
    node_l,
    node_m,
    node_n,
    node_o,
    node_p,
    node_q,
    node_r,
    node_s,
    node_t,
]

# 3. ALGORITMO DEL CAMINO MÁS CORTO (DIJKSTRA)
def dijkstra(start_node, target_node, nodes_list):
  # Distancia acumulada a cada nodo (inicialmente infinito)
  distances = {node: math.inf for node in nodes_list}
  # Guarda el nodo previo para reconstruir la ruta final
  previous = {node: None for node in nodes_list}
  # Lista de nodos pendientes por visitar
  unvisited = list(nodes_list)

  # La distancia a la ciudad de origen es 0
  distances[start_node] = 0

  while unvisited:
    # 1. Seleccionar el nodo no visitado con la menor distancia registrada
    current_node = min(unvisited, key=lambda node: distances[node])

    # Si la menor distancia es infinito o llegamos al destino, terminamos
    if distances[current_node] == math.inf or current_node == target_node:
      break

    unvisited.remove(current_node)

    # 2. Revisar los vecinos del nodo actual y actualizar distancias
    for edge in current_node.connections:
      neighbor = edge.destination
      if neighbor in unvisited:
        new_distance = distances[current_node] + edge.weight
        if new_distance < distances[neighbor]:
          distances[neighbor] = new_distance
          previous[neighbor] = current_node

  # 3. Reconstruir la ruta óptima desde el destino hacia el origen
  path = []
  curr = target_node
  while curr is not None:
    path.insert(0, curr)
    curr = previous[curr]

  return path, distances[target_node]

# 4. CALCULAR RUTA DE ARAD (node_r) A BUCHAREST (node_g)
shortest_path, total_distance = dijkstra(node_r, node_g, all_nodes)

# Imprimir resultados
path_names = " -> ".join([node.value for node in shortest_path])
print(f"Ruta más corta de Arad a Bucharest:")
print(f"Camino: {path_names}")
print(f"Distancia total: {total_distance} km\n")

# 5. DIBUJAR Y RESALTAR LA RUTA EN EL GRAFO
G = nx.Graph()
for node in all_nodes:
  for edge in node.connections:
    G.add_edge(edge.origin, edge.destination, weight=edge.weight)

positions = {
    node_a: (10.0, 7.0),
    node_b: (11.0, 6.0),
    node_c: (10.0, 5.0),
    node_d: (8.5, 4.0),
    node_e: (10.5, 3.5),
    node_f: (11.5, 2.5),
    node_g: (7.0, 3.0),
    node_h: (6.0, 1.5),
    node_i: (6.0, 5.5),
    node_j: (5.5, 4.0),
    node_k: (4.0, 6.0),
    node_l: (4.5, 4.5),
    node_m: (4.0, 2.5),
    node_n: (2.5, 2.0),
    node_o: (1.5, 3.0),
    node_p: (1.0, 4.0),
    node_q: (0.5, 5.0),
    node_r: (1.5, 6.5),
    node_s: (2.5, 7.5),
    node_t: (3.5, 8.0),
}

plt.figure(figsize=(14, 9))

# Identificar aristas que pertenecen a la ruta más corta
path_edges = [
    (shortest_path[i], shortest_path[i + 1])
    for i in range(len(shortest_path) - 1)
]

# Color de los nodos (resaltar los de la ruta)
node_colors = [
    "tomato" if node in shortest_path else "skyblue" for node in G.nodes()
]

# Color de las carreteras (resaltar las de la ruta)
edge_colors = [
    (
        "red"
        if (u, v) in path_edges or (v, u) in path_edges
        else "gray"
    )
    for u, v in G.edges()
]
edge_widths = [
    (
        3.5
        if (u, v) in path_edges or (v, u) in path_edges
        else 1.0
    )
    for u, v in G.edges()
]

# Dibujar grafo
nx.draw(
    G,
    positions,
    labels={node: node.value for node in G},
    with_labels=True,
    node_color=node_colors,
    edge_color=edge_colors,
    width=edge_widths,
    node_size=1500,
    font_size=9,
    font_weight="bold",
)

nx.draw_networkx_edge_labels(
    G,
    positions,
    edge_labels=nx.get_edge_attributes(G, "weight"),
    label_pos=0.5,
    font_size=8,
    bbox={"alpha": 0.8, "color": "white", "pad": 1},
)

plt.title(
    f"Ruta más corta: Arad -> Bucharest ({total_distance} km)",
    fontsize=14,
    fontweight="bold",
)
plt.axis("off")
plt.subplots_adjust(left=0.04, right=0.98, top=0.94, bottom=0.04)
plt.show()