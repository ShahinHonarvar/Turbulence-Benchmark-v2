import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.size(submatrix) == 57:
                        count += 1
    return count