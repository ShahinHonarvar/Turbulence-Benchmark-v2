import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    target_count = 146
    submatrix_count = 0
    rows, cols = matrix.shape
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    if np.prod((end_row - start_row, end_col - start_col)) == target_count:
                        submatrix_count += 1
    return submatrix_count