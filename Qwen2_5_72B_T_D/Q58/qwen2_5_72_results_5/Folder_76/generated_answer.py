import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    target_size = 159
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                if size * size == target_size:
                    submatrix = matrix[i:i + size, j:j + size]
                    count += 1
    return count if count else 0