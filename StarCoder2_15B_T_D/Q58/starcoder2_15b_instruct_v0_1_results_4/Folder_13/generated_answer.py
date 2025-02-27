import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 4):
        for j in range(n - 4):
            sub_matrix = matrix[i:i + 5, j:j + 5]
            if sub_matrix.size == 175:
                count += 1
    return count