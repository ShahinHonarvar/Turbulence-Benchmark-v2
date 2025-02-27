import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        submatrix_count = 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] == n:
                    submatrix_count += 1
        return submatrix_count
    rows, cols = matrix.shape
    submatrix_count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 80:
                submatrix_count += 1
    return submatrix_count