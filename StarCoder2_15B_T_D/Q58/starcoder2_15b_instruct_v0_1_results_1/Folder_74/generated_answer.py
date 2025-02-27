import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 6 + 1):
        for j in range(n - 6 + 1):
            submatrix = matrix[i:i + 6, j:j + 6]
            if submatrix.size == 48:
                count += 1
    return count