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
            print("Given density is too high to generate a graph without cycles. \nSo we have generated graph with max possible density")

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


class ListGraph:
    def get_size(self) -> int:
        return self.__size

    def get_edges(self) -> int:
        return sum(len(lst) for lst in self.adj_list.values())

    def __str__(self) -> str:
        result = ""
        for v, lst in self.adj_list.items():
            result += f"{v}: {lst}\n"
        return result


    def __dfs(self, v: int, visited: set, finished: set) -> bool:
        if v in finished:
            return False
        if v in visited:
            return True

        visited.add(v)
        cycle = False

        for u in self.adj_list[v]:
            if self.__dfs(u, visited, finished):
                cycle = True

        finished.add(v)
        return cycle

    def detect_cycle(self) -> bool:
        visited = set()
        finished = set()

        for v in range(self.get_size()):
            if v in visited:
                visited.remove(v)
            if v in finished:
                finished.remove(v)

            if self.__dfs(v, visited, finished):
                return True

        return False


    def __randomize(self, density: float):
        n = self.get_size()
        full_edges = n * (n - 1)
        generate_edges = int(full_edges * density)

        attempts = generate_edges * 10

        for _ in range(attempts):
            if generate_edges <= 0:
                return

            v1 = rd.randint(0, n - 1)
            v2 = rd.randint(0, n - 1)

            if v1 == v2:
                continue

            if v2 in self.adj_list[v1]:
                continue
            self.adj_list[v1].append(v2)
            if self.detect_cycle():
                self.adj_list[v1].remove(v2)
            else:
                generate_edges -= 1

        else:
            print("Given density is too high to generate a graph without cycles. \nSo we have generated graph with max possible density")

    def __init__(self, size: int, density: float, copy=None):
        if copy is None:
            self.__size = size
        else:
            self.__size = copy.get_size()

        self.adj_list = {i: [] for i in range(self.get_size())}

        if copy is not None:

            for v in range(self.get_size()):
                self.adj_list[v] = list(copy.adj_list[v])
        else:

            self.__randomize(density)

m = ListGraph(10, 0.1)
print(m)



