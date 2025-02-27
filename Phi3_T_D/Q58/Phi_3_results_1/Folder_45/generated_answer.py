import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if len(matrix.shape) != 2:
        raise ValueError('Input matrix must be two-dimensional')
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i + 27 < rows and j + 27 < cols:
                count += 1
    return count