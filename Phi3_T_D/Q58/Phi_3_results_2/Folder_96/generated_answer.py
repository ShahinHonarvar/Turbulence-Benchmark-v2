import numpy as np

def submatrix_with_n_numbers(matrix, n=20):
    m, n = matrix.shape
    count = 0
    for start_row in range(m):
        for start_col in range(n):
            for size_row in range(1, m - start_row + 1):
                for size_col in range(1, n - start_col + 1):
                    if size_row * size_col == n:
                        count += 1
    return count