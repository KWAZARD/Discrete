from conversion import *
from matrix_and_list_class import *
from kahn_for_matrix import *
from kahn_for_list import *
from visuals import *

try:
    vertices = int(input("Enter how many vertices Graph has: "))
    density = (float(input("Enter percents of Graph density: ")))/100
    max_edges = vertices * (vertices-1)
except ValueError:
    print("You need a number")

# m = MatrixGraph(vertices, density)
# g = ListGraph(vertices, density)
#
# print(f"Початково створена матриця: \n{m}")
# print(f"Кількість ребер в графі: {m.get_edges()}")
# print(f'''Перетворені з матриці списки суміжності:''')
# print(matrixgraph_to_listgraph(m))
#
#
# print(f"Початково створені списки суміжності: \n{g}")
# print(f"Кількість ребер в графі: {g.get_edges()}")
# print(f'''Перетворена з списка суміжності матриця:''')
# print(listgraph_to_matrixgraph(g))
#
# print(f'''Кан для матриці суміжності:''')
# print(kahn_for_matrix(m))
# print(f'''Кан для списків суміжності:''')
# print(kahn_for_list(g))


lt = ListGraph(5, 0.1)
k = listgraph_to_matrixgraph(lt)
print(kahn_for_list(lt))
print(kahn_for_matrix(k))


# visualize(m)