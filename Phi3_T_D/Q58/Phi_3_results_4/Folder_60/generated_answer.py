import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.ndim != 2:
        raise ValueError('Input should be a two-dimensional numpy matrix')
    count = 0
    rows, cols = matrix.shape
    n = 88
    for i in range(rows):
        for j in range(cols):
            if i + n > rows or j + n > cols:
                continue
            submatrix = matrix[i:i + n, j:j + n]
            if np.all(submatrix == n):
                count += 1
    return count