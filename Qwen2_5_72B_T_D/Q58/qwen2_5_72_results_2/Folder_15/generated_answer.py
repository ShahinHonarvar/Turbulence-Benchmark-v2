import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_two_numbers(matrix, n_rows, n_cols):
        count = 0
        for i in range(n_rows - 1 + 1):
            for j in range(n_cols - 1 + 1):
                if matrix[i:i + 1, j:j + 1].size == 2:
                    count += 1
        return count
    n_rows, n_cols = matrix.shape
    return count_submatrices_with_two_numbers(matrix, n_rows, n_cols)