import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        for i in range(mat.shape[0] - n + 1):
            for j in range(mat.shape[1] - n + 1):
                if mat[i:i + n, j:j + n].size == n:
                    count += 1
        return count
    n = 126
    return count_submatrices_with_n_elements(matrix, n)