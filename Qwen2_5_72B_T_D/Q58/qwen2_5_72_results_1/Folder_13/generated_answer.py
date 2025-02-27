import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 175
    total_rows, total_cols = matrix.shape
    valid_submatrices = 0
    for start_row in range(total_rows):
        for start_col in range(total_cols):
            for end_row in range(start_row, total_rows):
                for end_col in range(start_col, total_cols):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if submatrix.size == target_count:
                        valid_submatrices += 1
    return valid_submatrices