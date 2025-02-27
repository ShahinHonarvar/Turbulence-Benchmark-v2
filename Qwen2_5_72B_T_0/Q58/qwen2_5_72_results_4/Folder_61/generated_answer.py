import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        rows, cols = mat.shape
        count = 0
        for i in range(rows - 1):
            for j in range(cols - 1):
                submat = mat[i:i + 2, j:j + 2]
                if np.count_nonzero(submat) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 4)