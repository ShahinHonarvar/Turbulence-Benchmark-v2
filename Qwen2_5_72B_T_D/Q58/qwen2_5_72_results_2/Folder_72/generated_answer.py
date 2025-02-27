import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n(matrix, n=16):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if i + 4 <= rows and j + 4 <= cols and (np.sum(matrix[i:i + 4, j:j + 4]) == n):
                    count += 1
        return count
    return count_submatrices_with_n(matrix)