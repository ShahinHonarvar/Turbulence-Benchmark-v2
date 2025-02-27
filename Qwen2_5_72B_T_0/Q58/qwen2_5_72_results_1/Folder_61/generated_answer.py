import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        for i in range(mat.shape[0] - 1):
            for j in range(mat.shape[1] - 1):
                if np.unique(mat[i:i + 2, j:j + 2]).size == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 4)