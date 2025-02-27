import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a two-dimensional numpy matrix')
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for size in range(1, min(m - i, n - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.all(submatrix == 180):
                    count += 1
    return count