import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                submatrix_size = (rows - i) * (cols - j)
                if submatrix_size == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 159)