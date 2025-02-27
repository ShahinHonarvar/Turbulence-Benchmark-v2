import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2 or (not issubclass(matrix.dtype.type, np.integer)):
        raise ValueError('Input must be a two-dimensional numpy matrix of integers')
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                if 111 == np.sum(matrix[i:i + size, j:j + size]):
                    count += 1
    return count