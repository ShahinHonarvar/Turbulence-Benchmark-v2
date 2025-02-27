import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        row_count, col_count = mat.shape
        submatrix_count = 0
        for start_row in range(row_count):
            for start_col in range(col_count):
                for end_row in range(start_row + 1, row_count + 1):
                    for end_col in range(start_col + 1, col_count + 1):
                        if (end_row - start_row) * (end_col - start_col) == n:
                            submatrix_count += 1
        return submatrix_count
    return count_submatrices_with_n_elements(matrix, 20)