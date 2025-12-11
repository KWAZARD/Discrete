from matrix_and_list_class import *
from  kahn_for_matrix import *
from kahn_for_list import  *
import time

# Initialization
# tuple_exp_vertices = (20, 40, 60, 80, 100, 120, 140, 160, 180, 200)
tuple_exp_vertices = (20, 40)
tuple_exp_density = (0.1, 0.2, 0.3, 0.4, 0.5)
# experiments_per_combination = 20
experiments_per_combination = 3

total_iterations = len(tuple_exp_density) * len(tuple_exp_vertices) * experiments_per_combination * 2
count_iterations = 0

mat_resmat = []

# Experiments for Matrix
for i in range(len(tuple_exp_vertices)):
    mat_resmat.append([])
    for j in range(len(tuple_exp_density)):
        sum_of_times = 0
        for e in range(experiments_per_combination):
            exp_mat = MatrixGraph(tuple_exp_vertices[i], tuple_exp_density[j])
            start_time = time.time()
            kahn_for_matrix(exp_mat)
            stop_time = time.time()
            sum_of_times += stop_time - start_time
            count_iterations += 1
            print(f"{int(count_iterations / total_iterations * 100)} %")
        mat_resmat[i].append(sum_of_times/experiments_per_combination)

# Writing to file results for Matrix
resstr = ""
for i in mat_resmat:
    for j in i:
        resstr += f"{j:.06f},"
    resstr += "\n"

with open("matrix_experiments_results.csv", "w") as f:
    f.write(resstr)

list_resmat = []

# Experiments for Lists
for i in range(len(tuple_exp_vertices)):
    list_resmat.append([])
    for j in range(len(tuple_exp_density)):
        sum_of_times = 0
        for e in range(experiments_per_combination):
            exp_mat = ListGraph(tuple_exp_vertices[i], tuple_exp_density[j])
            start_time = time.time()
            kahn_for_list(exp_mat)
            stop_time = time.time()
            sum_of_times += stop_time - start_time
            count_iterations += 1
            print(f"{int(count_iterations / total_iterations * 100)} %")
        list_resmat[i].append(sum_of_times/experiments_per_combination)

# Writing to file results for Lists
resstr = ""
for i in list_resmat:
    for j in i:
        resstr += f"{j:.06f},"
    resstr += "\n"

with open("list_experiments_results.csv", "w") as f:
    f.write(resstr)