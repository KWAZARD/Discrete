from matrix_and_list_class import *
from conversion import *
import math
from pyvis.network import Network

def visualize(m) -> None:
    net = Network(height="900px", width="100%", bgcolor="#1e1e1e", font_color="white", directed=True)

    # --- додаємо вузли ---
    n = m.get_size()
    radius = 500

    for i in range(n):
        x = math.cos(i / n * 2 * math.pi) * radius
        y = math.sin(i / n * 2 * math.pi) * radius
        net.add_node(
            f"v{i}",
            label=f"v{i}",
            x=x,
            y=y,
            fixed=True,
            physics=False,
            size=5,
            color="#03DAC6"
        )

    # додаємо ребра
    if type(m) == ListGraph:
        matrix = listgraph_to_matrixgraph(m).matrix_list
    elif type(m) == MatrixGraph:
        matrix = m.matrix_list
    else:
        print("Invalid input type.")
        return
    
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 1:
                net.add_edge(f"v{i}", f"v{j}", width=0.5, color="#BB86FC")

    net.set_options("""
    var options = {
    "physics": {"enabled": false},
    "edges": {"smooth": false, "color": {"inherit": false}},
    "interaction": {"zoomView": true, "dragView": true, "navigationButtons": true, "hover": true},
    "nodes": {"shape": "dot", "font": {"size": 10}}
    }
    """)

    net.write_html("graph_visual.html", open_browser=True)