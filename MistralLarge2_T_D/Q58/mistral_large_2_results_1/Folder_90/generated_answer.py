import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, rows, cols, n):
        count = 0
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        if (k - i + 1) * (l - j + 1) == n:
                            count += 1
        return count
    rows, cols = matrix.shape
    return count_submatrices(matrix, rows, cols, 176)