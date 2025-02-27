import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        rows, cols = matrix.shape
        target_rows = int(np.ceil(n / cols))
        target_cols = int(np.ceil(n / rows))
        count = 0
        for i in range(rows - target_rows + 1):
            for j in range(cols - target_cols + 1):
                if np.prod(matrix[i:i + target_rows, j:j + target_cols].shape) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 48)