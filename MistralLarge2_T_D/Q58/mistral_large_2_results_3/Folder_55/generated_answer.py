import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i + 1, rows + 1):
                    for l in range(j + 1, cols + 1):
                        submatrix = matrix[i:k, j:l]
                        if submatrix.size == n:
                            count += 1
        return count
    return count_submatrices(matrix, 39)