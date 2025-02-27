import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 185

    def count_submatrices(r, c):
        if r >= rows or c >= cols:
            return 0
        if r * c < n:
            return 0
        if r * c == n:
            return 1
        return count_submatrices(r + 1, c) + count_submatrices(r, c + 1)
    return count_submatrices(1, 1)