import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 78
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                if matrix[i:i + size, j:j + size].size == target_count:
                    count += 1
    return count