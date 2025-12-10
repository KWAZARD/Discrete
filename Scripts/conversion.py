from matrix_and_list_class import *

def matrixgraph_to_listgraph(m: MatrixGraph) -> ListGraph:
    size = m.get_size()

    lg = ListGraph(size, 0)

    for i in range(size): # для написання цього циклу використано чат Гпт
        for j in range(size):
            if m.matrix_list[i][j] == 1:
                lg.adj_list[i].append(j)

    return lg

def listgraph_to_matrixgraph(g: ListGraph) -> MatrixGraph:
    size = g.get_size()

    mg = MatrixGraph(size, 0)

    for v in range(size): # для написання цього циклу використано чат Гпт
        for u in g.adj_list[v]:
            mg.matrix_list[v][u] = 1

    return mg