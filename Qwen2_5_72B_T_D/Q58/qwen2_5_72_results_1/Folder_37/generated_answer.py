import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(n_rows, n_cols, target_size):
        return (n_rows - target_size + 1) * (n_cols - target_size + 1)
    n_rows, n_cols = matrix.shape
    target_size = int(np.sqrt(64))
    if target_size * target_size != 64 or n_rows < target_size or n_cols < target_size:
        return 0
    return count_submatrices(n_rows, n_cols, target_size)