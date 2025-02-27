import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        row_count, col_count = matrix.shape
        submatrix_count = 0
        for start_row in range(row_count):
            for start_col in range(col_count):
                submatrix_size = (start_row + 1) * (start_col + 1)
                if submatrix_size == n:
                    submatrix_count += 1
        return submatrix_count
    return count_submatrices_with_n_elements(matrix, 130)