import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if np.prod(matrix[i:i + n, j:j + n].shape) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 66)