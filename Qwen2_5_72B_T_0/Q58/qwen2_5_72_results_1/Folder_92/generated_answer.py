import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        for i in range(len(mat) - 1):
            for j in range(len(mat[0]) - 1):
                if np.sum(mat[i:i + 2, j:j + 2] == n) == 8:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 8)