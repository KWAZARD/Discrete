from matrix_and_list_class import *

def __has_incoming_edges(m: MatrixGraph, v: int) -> bool:
    if v > m.get_size() or v < 0:
        return None
    for i in range(m.get_size()):
        if m.matrix_list[i][v] == 1:
            return True
    else:
        return False

def __vertices_with_no_incoming_edge(m: MatrixGraph) -> list:
    reslist = []
    for i in range(m.get_size()):
        if not __has_incoming_edges(m, i):
            reslist.append(i)
    return reslist

# Algorithm from https://en.wikipedia.org/wiki/Topological_sorting
def kahn_for_matrix(m: MatrixGraph) -> list:
    copy_mat = MatrixGraph(0, 0, m)
    l = []
    s = __vertices_with_no_incoming_edge(copy_mat)
    while len(s) > 0:
        n = s[0]
        s.pop(0)
        l.append(n)
        for i in range(copy_mat.get_size()):
            if copy_mat.matrix_list[n][i] == 1:
                copy_mat.matrix_list[n][i] = 0
                if not __has_incoming_edges(copy_mat, i):
                    s.append(i)
    return l
