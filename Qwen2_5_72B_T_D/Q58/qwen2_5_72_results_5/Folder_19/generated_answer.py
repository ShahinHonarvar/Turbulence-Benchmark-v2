import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(mat, n):
        count = 0
        for row in range(len(mat) - n + 1):
            for col in range(len(mat[0]) - n + 1):
                if np.prod(mat[row:row + n, col:col + n].shape) == 17:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 17)