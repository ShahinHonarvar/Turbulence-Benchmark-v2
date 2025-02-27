import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError('Input should be a numpy ndarray.')
    if len(matrix.shape) != 2:
        raise ValueError('Input should be a 2-dimensional matrix.')
    m, n = matrix.shape
    count = 0
    for sz in range(1, min(m, n) + 1):
        for i in range(m - sz + 1):
            for j in range(n - sz + 1):
                submatrix = matrix[i:i + sz, j:j + sz]
                if np.count_nonzero(submatrix) == sz ** 2:
                    count += 1
    return count