import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(28 - 1, min(m - i, n - j)):
                submatrix = matrix[i:i + size + 1, j:j + size + 1]
                if submatrix.size == 28:
                    count += 1
    return count