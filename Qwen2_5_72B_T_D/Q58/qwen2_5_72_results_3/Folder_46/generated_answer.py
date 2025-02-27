import numpy as np

def submatrix_with_n_numbers(matrix):
    total_rows, total_cols = matrix.shape
    target_size = 144
    submatrix_count = 0
    for start_row in range(total_rows - target_size + 1):
        for start_col in range(total_cols - target_size + 1):
            if start_row + 12 <= total_rows and start_col + 12 <= total_cols:
                submatrix = matrix[start_row:start_row + 12, start_col:start_col + 12]
                if submatrix.size == target_size:
                    submatrix_count += 1
    return submatrix_count