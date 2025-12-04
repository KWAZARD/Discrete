from classes import *
import matplotlib
from collections import namedtuple

try:
    vertices = int(input("Enter how many vertices Graph has: "))
    density = float(input("Enter percents of Graph density: "))/100
    max_edges = vertices * (vertices-1)
except ValueError:
    print("You need a number")

density_edges = density * max_edges
Graph = namedtuple("Graph", ["nodes", "edges"])

nodes = ["A","B","C","D"]
edges = [
    ("A", "B"),
    ("A", "B"),
    ("A", "C"),
    ("A", "C"),
    ("B", "D"),
    ("C", "D"),
]
G = Graph(nodes, edges)
def adjacency_dict(graph):
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)    
        adj[node2].append(node1)
    return adj
print(adjacency_dict(G))
