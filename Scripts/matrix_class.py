import random as rd

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
