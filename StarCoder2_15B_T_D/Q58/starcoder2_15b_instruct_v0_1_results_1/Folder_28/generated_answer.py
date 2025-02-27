import numpy as np

def submatrix_with_n_numbers(matrix, n=37):
    """
    Calculates the number of submatrices in `matrix` that contain `n` integers.
    """
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for row_start in range(num_rows):
        for col_start in range(num_cols):
            for row_end in range(row_start + 1, num_rows + 1):
                for col_end in range(col_start + 1, num_cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    num_submatrices += 1 if submatrix.size == n else 0
    return num_submatrices