from classes import *
import matplotlib
from collections import namedtuple
from matrix_class import *
from kahn_for_matrix import *
from covertation_of_graph import *

try:
    vertices = int(input("Enter how many vertices Graph has: "))
    density = float(input("Enter percents of Graph density: "))/100
    max_edges = vertices * (vertices-1)
except ValueError:
    print("You need a number")

density_edges = density * max_edges

m = MatrixGraph(vertices, density)
print(kahn(m))