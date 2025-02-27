import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                if i + n <= rows and j + n <= cols:
                    submatrix = matrix[i:i + n, j:j + n]
                    if np.size(submatrix) == 97:
                        count += 1
        return count
    return count_submatrices(matrix, 1)