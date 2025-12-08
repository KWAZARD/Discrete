import matplotlib
from collections import namedtuple
from matrix_and_list_class import *
from kahn_for_matrix import *



try:
    vertices = int(input("Enter how many vertices Graph has: "))
    density = (float(input("Enter percents of Graph density: ")))/100
    max_edges = vertices * (vertices-1)
except ValueError:
    print("You need a number")



m = MatrixGraph(vertices, density)
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