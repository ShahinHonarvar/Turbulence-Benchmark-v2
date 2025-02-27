import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    target_size = 144
    rows, cols = matrix.shape
    valid_submatrices = 0
    for start_row in range(rows - target_size // cols + 1):
        for start_col in range(cols - target_size % cols + 1):
            if start_row + target_size // cols <= rows and start_col + target_size % cols <= cols:
                if np.prod(matrix[start_row:start_row + target_size // cols, start_col:start_col + target_size % cols].shape) == target_size:
                    valid_submatrices += 1
    return valid_submatrices