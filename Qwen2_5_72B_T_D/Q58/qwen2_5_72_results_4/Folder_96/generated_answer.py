import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        rows, cols = mat.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(1, rows - i + 1):
                    for l in range(1, cols - j + 1):
                        if k * l == n:
                            submatrix = mat[i:i + k, j:j + l]
                            count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 20)