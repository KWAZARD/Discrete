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
lg = ListGraph(vertices, density)
print(kahn(m))

print(f"Початково створена матриця: \n{m}")
print(f"Кількість ребер в матриці: {m.get_edges()}")
dict_adjacency = {}
def matrix_to_adjacency_list():           # З матриці -> Список суміжності
    lst_adjacency = []
    for i in range(0, len(m.matrix_list)):
        for j in range(0, len(m.matrix_list)):
            if m.matrix_list[i][j] == 1:
                lst_adjacency.append(f"v{j}")
        dict_adjacency.setdefault(f"v{i}", lst_adjacency)
        lst_adjacency = []
    print(f"Список суміжності: {dict_adjacency}")
matrix_to_adjacency_list()

def adjacency_list_to_matrix(adjacency_list):
    n = len(adjacency_list)                            # Ці рядки коду
    adjacency_matrix = [[0] * n for _ in range(n)]     # допоміг написати чатГПТ

    for i in range(n):
        for v in adjacency_list[f"v{i}"]:
            j = int(v[1:])
            adjacency_matrix[i][j] = 1

    return adjacency_matrix

print(f'''Перетворена з списка суміжності матриця:''')
for row in adjacency_list_to_matrix(dict_adjacency):
    print(row)


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
matrix = adjacency_list_to_matrix(dict_adjacency)
for i in range(len(matrix)):
    for j in range(len(matrix)):
        if matrix[i][j] == 1:
            net.add_edge(f"v{i}", f"v{j}", width=1, color="#BB86FC")

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
