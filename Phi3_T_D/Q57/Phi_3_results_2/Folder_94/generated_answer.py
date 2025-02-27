import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if len(matrix.shape) != 2 or not matrix.shape[0] or (not matrix.shape[1]):
        raise ValueError('Matrix must be non-empty 2D')
    target_sum = 92
    submatrices = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for row_end in range(row_start, rows):
                for col_end in range(col_start, cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix)
    return submatrices