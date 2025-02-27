import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n, size=64):
        count = 0
        for i in range(m - 8 + 1):
            for j in range(n - 8 + 1):
                submatrix = matrix[i:i + 8, j:j + 8]
                if submatrix.size == size:
                    count += 1
        return count
    m, n = matrix.shape
    return count_submatrices(m, n)