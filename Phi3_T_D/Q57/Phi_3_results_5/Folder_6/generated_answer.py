import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return []
    total_rows, total_cols = matrix.shape
    zero_matrix = np.zeros_like(matrix)
    found_submatrices = []
    for top_row in range(total_rows):
        for left_col in range(total_cols):
            for bottom_row in range(top_row, total_rows):
                for right_col in range(left_col, total_cols):
                    submatrix_sum = np.sum(matrix[top_row:bottom_row + 1, left_col:right_col + 1])
                    if submatrix_sum == 126:
                        found_submatrices.append(matrix[top_row:bottom_row + 1, left_col:right_col + 1])
    return found_submatrices