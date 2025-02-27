import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, cols = matrix.shape
    for row_start in range(rows):
        for col_start in range(cols):
            for subrows in range(1, rows - row_start + 1):
                for subcols in range(1, cols - col_start + 1):
                    current_submatrix = matrix[row_start:row_start + subrows, col_start:col_start + subcols]
                    if current_submatrix.size == 107:
                        submatrix_count += 1
    return submatrix_count