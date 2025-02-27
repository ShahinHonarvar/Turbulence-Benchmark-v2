import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m - 19):
        for j in range(n - 19):
            submatrix = matrix[i:i + 20, j:j + 20]
            if submatrix.size == 20:
                count += 1
    return count