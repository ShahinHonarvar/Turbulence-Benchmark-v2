import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows):
        for j in range(num_cols):
            if i + 95 <= num_rows and j + 95 <= num_cols:
                count += 1
    return count