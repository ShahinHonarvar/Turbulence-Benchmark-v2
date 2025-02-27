import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 180
    row, col = matrix.shape
    valid_submatrices = 0
    for start_row in range(row - 13 + 1):
        for start_col in range(col - 13 + 1):
            if np.sum((matrix[start_row:start_row + 13, start_col:start_col + 13] != 0).astype(int)) == target_count:
                valid_submatrices += 1
    return valid_submatrices