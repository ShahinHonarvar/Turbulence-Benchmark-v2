import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy ndarray')
    if len(matrix.shape) != 2:
        raise ValueError('Matrix must be two-dimensional')
    h, w = matrix.shape
    count = 0
    for size in range(1, min(h, w) + 1):
        for x in range(h - size + 1):
            for y in range(w - size + 1):
                count += np.all(matrix[x:x + size, y:y + size] == 24)
    return count