import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_two_elements(mat):
        count = 0
        rows, cols = mat.shape
        for i in range(rows - 1):
            for j in range(cols - 1):
                if np.unique(mat[i:i + 2, j:j + 2]).size == 2:
                    count += 1
        return count
    return count_submatrices_with_two_elements(matrix)