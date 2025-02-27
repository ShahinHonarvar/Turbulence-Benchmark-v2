import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('The argument must be a two-dimensional numpy matrix.')
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            sub_matrix = matrix[i:i + 2, j:j + 2]
            if sub_matrix.size == 74:
                count += 1
    return count