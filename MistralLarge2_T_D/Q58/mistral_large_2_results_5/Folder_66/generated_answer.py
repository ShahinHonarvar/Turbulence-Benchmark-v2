import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(n, m, k):
        if k == 0:
            return 1
        if n == 0 or m == 0 or k < 0:
            return 0
        return count_submatrices(n - 1, m, k) + count_submatrices(n, m - 1, k) - count_submatrices(n - 1, m - 1, k)
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if (x - i + 1) * (y - j + 1) == 42:
                        count += 1
    return count