import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                submat = mat[i:i + 10, j:j + 10]
                if submat.size == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 93)