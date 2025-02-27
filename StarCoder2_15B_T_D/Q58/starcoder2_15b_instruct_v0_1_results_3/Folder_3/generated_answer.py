import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy array.')
    rows, columns = matrix.shape
    count = 0
    for i in range(rows - 2):
        for j in range(columns - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 54:
                count += 1
    return count