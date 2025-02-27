import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if matrix.ndim != 2:
        raise ValueError('Input must be a two-dimensional numpy matrix')
    m, n = matrix.shape
    count = 0
    for size in range(min(m, n), 0, -1):
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == size * size == 27:
                    count += 1
    return count