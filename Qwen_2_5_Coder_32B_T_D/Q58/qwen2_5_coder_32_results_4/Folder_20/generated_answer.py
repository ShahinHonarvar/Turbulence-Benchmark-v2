import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m - 6):
        for j in range(n - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == 49:
                count += 1
    return count