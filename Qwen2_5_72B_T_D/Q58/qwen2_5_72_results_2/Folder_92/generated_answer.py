import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        for i in range(len(mat) - 1):
            for j in range(len(mat[0]) - 1):
                if mat[i][j] + mat[i][j + 1] + mat[i + 1][j] + mat[i + 1][j + 1] == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 8)