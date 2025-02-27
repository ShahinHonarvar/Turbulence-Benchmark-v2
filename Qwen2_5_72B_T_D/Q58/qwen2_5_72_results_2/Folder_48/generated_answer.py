import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                if (i + 1) * (j + 1) == n:
                    count += 1
                elif (rows - i) * (cols - j) >= n:
                    submat = mat[i:rows, j:cols]
                    if submat.size == n:
                        count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 130)