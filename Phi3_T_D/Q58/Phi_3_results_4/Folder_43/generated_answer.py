import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    count_85 = 0
    for row_start in range(matrix.shape[0]):
        for col_start in range(matrix.shape[1]):
            for submatrix_size in range(1, min(matrix.shape) + 1):
                if row_start + submatrix_size > matrix.shape[0] or col_start + submatrix_size > matrix.shape[1]:
                    break
                submatrix = matrix[row_start:row_start + submatrix_size, col_start:col_start + submatrix_size]
                if submatrix.size == 85:
                    count_85 += 1
    return count_85