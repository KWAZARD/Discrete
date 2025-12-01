from classes import *
import matplotlib

try:
    vertices = int(input("Enter how many vertices Graph has: "))
    density = float(input("Enter percents of Graph density: "))/100
    max_edges = vertices * (vertices-1)
except ValueError:
    print("You need a number")

density_edges = density * max_edges
Graph1 = Graph(max_edges, density)
Graph1.graph_draw()