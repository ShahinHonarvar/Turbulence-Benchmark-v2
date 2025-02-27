import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 73
    total_rows, total_cols = matrix.shape
    count = 0
    for start_row in range(total_rows):
        for start_col in range(total_cols):
            for end_row in range(start_row, total_rows):
                for end_col in range(start_col, total_cols):
                    if (end_row - start_row + 1) * (end_col - start_col + 1) == target_count:
                        count += 1
    return count