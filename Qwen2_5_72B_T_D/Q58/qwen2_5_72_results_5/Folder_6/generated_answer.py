import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if i + 10 <= rows and j + 12 <= cols and (np.sum(matrix[i:i + 10, j:j + 12] == 122) == n):
                    count += 1
        return count
    return count_submatrices_with_n(matrix, 122)