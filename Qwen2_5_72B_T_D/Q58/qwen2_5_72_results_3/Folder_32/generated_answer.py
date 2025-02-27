import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        for i in range(matrix.shape[0] - n + 1):
            for j in range(matrix.shape[1] - n + 1):
                submatrix = matrix[i:i + n, j:j + n]
                if submatrix.size == n:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 103)