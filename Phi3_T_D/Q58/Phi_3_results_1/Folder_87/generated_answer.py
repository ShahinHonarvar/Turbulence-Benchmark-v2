import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        raise ValueError('Input must be a 2D numpy matrix.')
    count = 0
    n = matrix.shape[0]
    m = matrix.shape[1]
    for i in range(n):
        for j in range(m):
            for k in range(i + 1, n + 1):
                rows = k - i
                for l in range(j + 1, m + 1):
                    cols = l - j
                    if rows * cols == 96:
                        count += 1
    return count