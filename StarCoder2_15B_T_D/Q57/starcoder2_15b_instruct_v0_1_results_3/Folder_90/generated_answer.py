import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if sub_matrix.sum() == -452:
                result.append(sub_matrix)
    return result