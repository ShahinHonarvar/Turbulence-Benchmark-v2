import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 126:
                        count += 1
    return count