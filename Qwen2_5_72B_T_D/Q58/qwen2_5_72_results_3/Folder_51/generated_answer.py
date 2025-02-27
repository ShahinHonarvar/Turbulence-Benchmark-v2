import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if np.prod(mat[i:i + n, j:j + n].shape) == n:
                    count += 1
        return count if count else 0
    return count_submatrices_with_n_elements(matrix, 95)