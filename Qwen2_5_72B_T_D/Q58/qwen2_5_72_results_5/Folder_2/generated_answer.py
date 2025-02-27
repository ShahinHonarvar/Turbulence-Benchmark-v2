import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                submat_size = 1
                while i + submat_size <= rows and j + submat_size <= cols:
                    submat = mat[i:i + submat_size, j:j + submat_size]
                    if submat.size == n:
                        count += 1
                    submat_size += 1
        return count
    return count_submatrices_with_n_elements(matrix, 107)