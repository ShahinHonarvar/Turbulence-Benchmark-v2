import numpy as np
from itertools import product

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a two-dimensional numpy matrix')
    n = 166
    row, col = matrix.shape
    count = 0
    for i, j, k, l in product(range(row), range(col), range(row), range(col)):
        submatrix_size = (k - i + 1, l - j + 1)
        if submatrix_size[0] * submatrix_size[1] == n:
            submatrix = matrix[i:i + k, j:j + l]
            submatrix_elements = np.sum(submatrix > 0)
            if submatrix_elements == n:
                count += 1
    return count