import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for r in range(rows):
            for c in range(cols):
                if (r + 1) * (c + 1) == n or (rows - r) * (cols - c) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 13)