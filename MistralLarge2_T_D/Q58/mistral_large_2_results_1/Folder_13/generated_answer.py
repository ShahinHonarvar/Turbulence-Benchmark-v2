import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 175

    def count_submatrices(r, c, n):
        if r + c - 1 < n:
            return 0
        if n == 0:
            return 1
        if n < 0:
            return 0
        return count_submatrices(r - 1, c, n - matrix[r - 1, c - 1]) + count_submatrices(r, c - 1, n) - count_submatrices(r - 1, c - 1, n)
    total_submatrices = 0
    for i in range(rows):
        for j in range(cols):
            total_submatrices += count_submatrices(i + 1, j + 1, n)
    return total_submatrices