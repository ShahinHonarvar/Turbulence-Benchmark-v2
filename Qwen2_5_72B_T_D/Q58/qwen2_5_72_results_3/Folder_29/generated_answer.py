import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    count += 1
                elif (rows - i) * (j + 1) >= n:
                    continue
                elif (cols - j) * (i + 1) >= n:
                    continue
        return count
    return count_submatrices_with_n_elements(matrix, 19)