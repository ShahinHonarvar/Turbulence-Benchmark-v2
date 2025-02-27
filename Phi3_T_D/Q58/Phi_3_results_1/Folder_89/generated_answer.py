import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix of integers.')
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k1 in range(i, rows):
                for l1 in range(j, cols):
                    submatrix = matrix[i:k1 + 1, j:l1 + 1]
                    if submatrix.size == 18:
                        submatrix_count += 1
    return submatrix_count