import random as rd


class MatrixGraph:
    def get_size(self) -> int:
        return self.__size
    
    def get_edges(self) -> int:
        result = 0
        for v in self.matrix_list:
            result += sum(v)
        return result

    def __str__(self) -> str:
        result = ""
        for i in range(self.get_size()):
            for j in range(self.get_size()):
                result += str(self.matrix_list[i][j]) + "|"
            result += "\n"
        return result

    # DFS-based cycle detection algorithm from https://en.wikipedia.org/wiki/Cycle_(graph_theory)
    def __dfs(self, v_number: int, visited_list: list, finished_list: list) -> bool:

        if v_number in finished_list:
            return False
        if v_number in visited_list:
            return True
        visited_list.append(v_number)
        result = 0
        for i in range(self.get_size()):
            if self.matrix_list[v_number][i] == 1:
                result += int(self.__dfs(i, visited_list, finished_list))
        finished_list.append(v_number)
        return bool(result)

    def detect_cycle(self) -> bool:
        result = 0
        visited_list = []
        finished_list = []
        for i in range(self.get_size()):
            if i in visited_list:
                visited_list.remove(i)
            if i in finished_list:
                finished_list.remove(i)
            result += int(self.__dfs(i, visited_list, finished_list))
        return bool(result)
    
    # Erdos-Renyi-based random graph generation
    def __randomize(self, density: float) -> None:
        graph_size = self.get_size()
        full_graph_edges = graph_size * (graph_size - 1)
        generate_edges = int(full_graph_edges * density)
        for i in range(generate_edges * 10):
            if generate_edges <= 0:
                return
            v1, v2 = rd.randint(0, graph_size - 1), rd.randint(0, graph_size - 1)
            if self.matrix_list[v1][v2] == 1:
                continue
            self.matrix_list[v1][v2] = 1
            if self.detect_cycle():
                self.matrix_list[v1][v2] = 0
            else:
                generate_edges -= 1
        else:
            print("Given density is too large to generate a graph without cycles.")
    
    def __init__(self, size: int, density: float, copy=None) -> None:
        if copy == None:
            self.__size = size
        else:
            self.__size = copy.get_size()
        self.matrix_list = []
        for i in range(self.get_size()):
            self.matrix_list.append([])
            for j in range(self.get_size()):
                if copy == None:
                    self.matrix_list[i].append(0)
                else:
                    self.matrix_list[i].append(copy.matrix_list[i][j])
        if copy == None:
            self.__randomize(density)



