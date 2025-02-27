import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    count = 0
    rows, cols = matrix.shape
    n = 78
    for row_start in range(rows - n + 1):
        for col_start in range(cols - n + 1):
            submatrix = matrix[row_start:row_start + n, col_start:col_start + n]
            if submatrix.size == n * n:
                count += 1
    return count