import numpy as np

def submatrix_with_n_numbers(matrix):
    total_rows, total_cols = matrix.shape
    target_size = 90
    valid_submatrix_count = 0
    for size in range(1, min(total_rows, total_cols) + 1):
        for row in range(total_rows - size + 1):
            for col in range(total_cols - size + 1):
                if np.prod(matrix[row:row + size, col:col + size].shape) == target_size:
                    valid_submatrix_count += 1
    return valid_submatrix_count