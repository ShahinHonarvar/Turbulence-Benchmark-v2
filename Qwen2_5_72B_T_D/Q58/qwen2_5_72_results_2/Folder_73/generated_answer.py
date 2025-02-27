import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        if n == 1:
            return rows * cols
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if mat[i:i + n, j:j + n].size == 41:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 41)