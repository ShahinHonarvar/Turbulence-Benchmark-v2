import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            sub_matrix = matrix[i:i + 1, j:j + 1]
            if sub_matrix.size == 139:
                count += 1
    return count