import numpy as np

def submatrix_with_n_numbers(matrix):
    total_rows, total_cols = matrix.shape
    target_size = 127
    count = 0
    for start_row in range(total_rows):
        for start_col in range(total_cols):
            if start_row + target_size <= total_rows and start_col + target_size <= total_cols:
                if matrix[start_row:start_row + target_size, start_col:start_col + target_size].size == target_size:
                    count += 1
    return count