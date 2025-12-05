import random as rd
from xmlrpc.client import MAXINT


class Matrix:
    def __init__(self, size: int):
        self.__size = size
        self.matrix_list = []
        for i in range(self.__size):
            self.matrix_list.append([])
            for j in range(self.__size):
                self.matrix_list[i].append(0)

    def get_size(self):
        return self.__size

    def __str__(self):
        result = ""
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                result += str(self.matrix_list[i][j]) + "|"
            result += "\n"
        return result

    def randomize(self):
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                if i == j:
                    continue
                self.matrix_list[i][j] = rd.randint(0, 1)


def multiply(m1: Matrix, m2: Matrix):
    size = m1.get_size()
    if size != m2.get_size():
        return
    resmat = Matrix(size)
    for i in range(size):
        for j in range(size):
            pass


m1 = Matrix(5)
m1.randomize()
print(m1)
print(m1.matrix_list)
dict_adjacency = {}
def matrix_to_adjacency_list():           # З матриці -> Список суміжності
    lst_adjacency = []
    for i in range(0, len(m1.matrix_list)):
        for j in range(0, len(m1.matrix_list)):
            if m1.matrix_list[i][j] == 1:
                lst_adjacency.append(f"v{j}")
        dict_adjacency.setdefault(f"v{i}", lst_adjacency)
        lst_adjacency = []
    print(dict_adjacency)
matrix_to_adjacency_list()

def adjency_list_to_matrix(dict_adjacency):    # з списку суміжності -> в матрицю
    size = len(dict_adjacency)
    matrix  = Matrix(size)
    for i in range(size):
        for v in dict_adjacency[f"v{i}"]:
            j = int(v[1:])
            matrix.matrix_list[i][j] = 1
    return matrix

print(adjency_list_to_matrix(dict_adjacency))
