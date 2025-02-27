import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if i + n <= rows and j + n <= cols:
                    if np.unique(matrix[i:i + n, j:j + n]).size == n:
                        count += 1
        return count
    return count_submatrices_of_size(matrix, 5)