import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input should be a numpy matrix')
    rows, cols = matrix.shape
    count = 0
    target_size = 118
    for i in range(rows):
        for j in range(cols):
            for n_rows in range(rows - i + 1):
                for n_cols in range(cols - j + 1):
                    if n_rows * n_cols == target_size:
                        count += 1
    return count