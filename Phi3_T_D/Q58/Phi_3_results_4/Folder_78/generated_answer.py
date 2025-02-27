import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    if m * n < 91:
        return 0
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 91:
                    count += 1
    return count