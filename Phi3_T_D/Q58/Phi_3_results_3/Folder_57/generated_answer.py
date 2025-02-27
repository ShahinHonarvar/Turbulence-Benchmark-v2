import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = matrix.shape[0] * matrix.shape[1]
    if n != 92:
        return 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.size == 92:
                        count += 1
    return count