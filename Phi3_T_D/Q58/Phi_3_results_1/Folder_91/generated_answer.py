import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    n = len(matrix)
    m = len(matrix[0])
    submatrix_count = 0
    for i in range(n):
        for j in range(m):
            for size in range(1, min(n - i, m - j) + 1):
                if size == 5:
                    submatrix_count += 1
                else:
                    submatrix_count += size ** 2
    return submatrix_count