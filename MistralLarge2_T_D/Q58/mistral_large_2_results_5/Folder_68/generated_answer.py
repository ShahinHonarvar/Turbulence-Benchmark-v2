import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 74

    def count_submatrices(r, c, k):
        if k == 0:
            return 1
        count = 0
        for i in range(r, rows):
            for j in range(c, cols):
                count += count_submatrices(i + 1, j, k - 1)
        return count
    total_count = 0
    for i in range(rows):
        for j in range(cols):
            total_count += count_submatrices(i, j, n)
    return total_count