import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2 or matrix.dtype != np.int:
        raise ValueError('Input must be a two-dimensional numpy matrix of integers.')
    count = 0
    rows, cols = matrix.shape
    size = 3
    for i in range(rows - size + 1):
        for j in range(cols - size + 1):
            if np.all(matrix[i:i + size, j:j + size]):
                count += 1
    return count