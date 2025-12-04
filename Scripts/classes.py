import matplotlib
import random

from matplotlib import pyplot as plt


class Graph:
    def __init__(self, vertices, max_edges, density):
        self.vertices = vertices
        self.max_edges = max_edges
        self.density = density
        self.vertex_list = []
    def graph_draw(self):
        graphs_edges = self.vertices * self.density # if n 100 graph_edges = 990
        return print(graphs_edges)
    def matrix_create(self):
        with open("Matrix.txt", "w") as matrix:
            matrix.write("  ")
            for i in range(1, self.vertices + 1):
                matrix.write(f"{i}".rjust(3))
            for i in range(1, self.vertices + 1):
                matrix.write(f"\n{i} ".rjust(4)+"|")

    def dfs_check(self):
        pass
graph = Graph(10, 90, 10)
graph.matrix_create()