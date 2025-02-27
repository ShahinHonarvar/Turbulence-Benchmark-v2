import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 73:
                    count += 1
    return count