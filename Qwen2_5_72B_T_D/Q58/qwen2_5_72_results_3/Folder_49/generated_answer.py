import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    submatrix_count = 0
    target_size = 72
    rows, cols = matrix.shape
    for start_row in range(rows - 8 + 1):
        for start_col in range(cols - 9 + 1):
            submatrix = matrix[start_row:start_row + 8, start_col:start_col + 9]
            if submatrix.size == target_size:
                submatrix_count += 1
    return submatrix_count