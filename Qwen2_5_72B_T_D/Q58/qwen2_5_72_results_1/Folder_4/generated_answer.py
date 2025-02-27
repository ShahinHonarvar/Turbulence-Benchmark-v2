import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                for row_end in range(i + 1, mat.shape[0] + 1):
                    for col_end in range(j + 1, mat.shape[1] + 1):
                        if (row_end - i) * (col_end - j) == n:
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 15)