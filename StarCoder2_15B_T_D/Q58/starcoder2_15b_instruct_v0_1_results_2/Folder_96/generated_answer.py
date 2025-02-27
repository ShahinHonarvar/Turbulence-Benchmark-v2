import numpy as np

def submatrix_with_n_numbers(matrix):
    num_rows, num_cols = matrix.shape
    num_numbers = 20
    num_submatrices = 0
    for row_start in range(num_rows - 1):
        for row_end in range(row_start + 1, num_rows):
            for col_start in range(num_cols - 1):
                for col_end in range(col_start + 1, num_cols):
                    submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    num_elements = submatrix.size
                    if num_elements == num_numbers:
                        num_submatrices += 1
    return num_submatrices