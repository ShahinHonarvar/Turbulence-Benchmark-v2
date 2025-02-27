import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise TypeError('The argument must be a two-dimensional numpy matrix.')
    if matrix.ndim != 2:
        raise ValueError('The argument must be a two-dimensional numpy matrix.')
    count = 0
    m, n = matrix.shape
    for i in range(m - 2):
        for j in range(n - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if sub_matrix.size == 72:
                count += 1
    return count