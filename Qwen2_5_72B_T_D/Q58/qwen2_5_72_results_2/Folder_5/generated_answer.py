import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n, k):
        count = 0
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                submatrix = matrix[i:i + k, j:j + k]
                if submatrix.size == 63:
                    count += 1
        return count
    m, n = matrix.shape
    return count_submatrices(m, n, 7)