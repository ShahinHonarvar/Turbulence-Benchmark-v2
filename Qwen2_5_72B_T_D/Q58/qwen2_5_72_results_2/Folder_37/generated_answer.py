import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(n_rows, n_cols, sub_n):
        count = 0
        for i in range(n_rows - sub_n + 1):
            for j in range(n_cols - sub_n + 1):
                if np.prod(matrix[i:i + sub_n, j:j + sub_n].shape) == 64:
                    count += 1
        return count
    n_rows, n_cols = matrix.shape
    return count_submatrices(n_rows, n_cols, 8)