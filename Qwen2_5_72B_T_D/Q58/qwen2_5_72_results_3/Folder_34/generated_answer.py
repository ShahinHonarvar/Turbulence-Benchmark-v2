import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                submatrix = mat[i:rows, j:cols]
                if submatrix.size == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 83)