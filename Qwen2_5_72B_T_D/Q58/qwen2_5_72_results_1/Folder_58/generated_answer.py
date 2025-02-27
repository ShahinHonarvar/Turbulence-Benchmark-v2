import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_k_elements(mat, k):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (rows - i) * (cols - j) == k:
                    count += 1
        return count
    return count_submatrices_with_k_elements(matrix, 185)