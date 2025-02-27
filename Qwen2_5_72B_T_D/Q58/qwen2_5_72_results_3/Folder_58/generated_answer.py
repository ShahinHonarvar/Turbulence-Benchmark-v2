import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 185
    rows, cols = matrix.shape
    if rows * cols < target_count:
        return 0
    valid_submatrices = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    submatrix = matrix[start_row:end_row, start_col:end_col]
                    if submatrix.size == target_count:
                        valid_submatrices += 1
    return valid_submatrices