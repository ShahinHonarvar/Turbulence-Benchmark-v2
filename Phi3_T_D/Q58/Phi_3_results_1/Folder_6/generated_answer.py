import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    rows, cols = matrix.shape
    if rows < 122 or cols < 122:
        return 0

    def count_submatrices(row_start, col_start, rows_needed, cols_needed):
        if rows_needed <= 0 or cols_needed <= 0:
            return 1
        current_count = 0
        for row in range(row_start, rows):
            for col in range(col_start, cols):
                top = row_start if row == row_start else row
                bottom = row + rows_needed - 1
                left = col_start if col == col_start else col
                right = col + cols_needed - 1
                total_sum = int(matrix[top:bottom + 1, left:right + 1].sum())
                if total_sum == 122:
                    current_count += 1
        return current_count + count_submatrices(row_start, col_start + 1, rows_needed, cols_needed - 1) + count_submatrices(row_start + 1, col_start, rows_needed - 1, cols_needed)
    total_count = 0
    for rows_needed in range(1, rows + 1):
        for cols_needed in range(1, cols + 1):
            total_count += count_submatrices(0, 0, rows_needed, cols_needed)
    return total_count