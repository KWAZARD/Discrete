import matplotlib
import random

from matplotlib import pyplot as plt


class Graph:
    def __init__(self, max_edges, density):
        self.vertices = max_edges
        self.density = density
        self.vertex_list = []
    def graph_draw(self):
        graphs_edges = self.vertices * self.density # if n 100 graph_edges = 990
        return print(graphs_edges)

    def dfs_check(self):
        pass