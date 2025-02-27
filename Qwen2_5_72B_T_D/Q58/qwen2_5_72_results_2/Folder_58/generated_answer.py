import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 185
    rows, cols = matrix.shape
    matching_submatrices = 0
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if np.prod(matrix[start_row:end_row, start_col:end_col].shape) == target_count:
                        matching_submatrices += 1
    return matching_submatrices