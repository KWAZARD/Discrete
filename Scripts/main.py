import matplotlib
from collections import namedtuple
import pyvis
import math
from pyvis.network import Network

from matrix_and_list_class import *
from kahn_for_matrix import *



try:
    vertices = int(input("Enter how many vertices Graph has: "))
    density = (float(input("Enter percents of Graph density: ")))/100
    max_edges = vertices * (vertices-1)
except ValueError:
    print("You need a number")



m = MatrixGraph(vertices, density)
g = ListGraph(vertices, density)

print(f"Початково створена матриця: \n{m}")
print(f"Кількість ребер в матриці: {m.get_edges()}")



def matrixgraph_to_listgraph(m: MatrixGraph) -> ListGraph:
    size = m.get_size()

    lg = ListGraph(size, 0)

    for i in range(size): # для написання цього циклу використано чат Гпт
        for j in range(size):
            if m.matrix_list[i][j] == 1:
                lg.adj_list[i].append(j)

    return lg
print(matrixgraph_to_listgraph(m))
def listgraph_to_matrixgraph(g: ListGraph) -> MatrixGraph:
    size = g.get_size()

    mg = MatrixGraph(size, 0)

    for v in range(size): # для написання цього циклу використано чат Гпт
        for u in g.adj_list[v]:
            mg.matrix_list[v][u] = 1

    return mg

print(f'''Перетворена з списка суміжності матриця:''')
print(listgraph_to_matrixgraph(g))



net = Network(height="900px", width="100%", bgcolor="#1e1e1e", font_color="white", directed=True)

# --- додаємо вузли ---
n = m.get_size()
cols = math.ceil(math.sqrt(n))   # кількість колонок у сітці
rows = math.ceil(n / cols)
spacing = 150                    # відстань між вузлами

for i in range(n):
    row = i // cols
    col = i % cols
    x = col * spacing
    y = row * spacing
    net.add_node(
        f"v{i}",
        label=f"v{i}",
        x=x,
        y=y,
        fixed=True,
        physics=False,
        size=16,
        color="#03DAC6"
    )

# --- додаємо ребра ---
# matrix = listgraph_to_matrixgraph(g)
# for i in range(len(matrix)):
#     for j in range(len(matrix)):
#         if matrix[i][j] == 1:
#             net.add_edge(f"v{i}", f"v{j}", width=1, color="#BB86FC")

# --- відключаємо фізику ---
net.set_options("""
var options = {
  "physics": {"enabled": false},
  "edges": {"smooth": false, "color": {"inherit": false}},
  "interaction": {"zoomView": true, "dragView": true, "navigationButtons": true, "hover": true},
  "nodes": {"shape": "dot", "font": {"size": 10}}
}
""")

net.write_html("graph_visual.html", open_browser=True)
