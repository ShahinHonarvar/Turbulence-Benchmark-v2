import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        if n == 1:
            return rows * cols
        for r in range(rows - n + 1):
            for c in range(cols - n + 1):
                if mat[r:r + n, c:c + n].size == 93:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 1)