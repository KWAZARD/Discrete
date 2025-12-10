from matrix_and_list_class import *

def __has_incoming_edges(g: ListGraph, v: int) -> bool:
    if v >= g.get_size() or v < 0:
        return None
    for u in range(g.get_size()):
        if v in g.adj_list[u]:    # якщо знайдено ребро u → v
            return True
    return False

def __vertices_with_no_incoming_edge(g: ListGraph) -> list:
    reslist = []
    for v in range(g.get_size()):
        if not __has_incoming_edges(g, v):
            reslist.append(v)
    return reslist

# Algorithm from https://en.wikipedia.org/wiki/Topological_sorting
def kahn_for_list(ls: ListGraph) -> list:
    copy_ls = ListGraph(10, 0.1)
    l = []
    s = __vertices_with_no_incoming_edge(copy_ls)
    while len(s) > 0:
        n = s[0]
        s.pop(0)
        l.append(n)
        for i in list(copy_ls.adj_list[n]):
            copy_ls.adj_list[n].remove(i)
            if not __has_incoming_edges(copy_ls, i):
                s.append(i)
    return l