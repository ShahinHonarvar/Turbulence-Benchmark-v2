import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        row_count, col_count = matrix.shape
        submatrix_count = (row_count - int(np.sqrt(n)) + 1) * (col_count - int(np.sqrt(n)) + 1)
        return submatrix_count if submatrix_count > 0 else 0
    return count_submatrices_with_n_elements(matrix, 95)