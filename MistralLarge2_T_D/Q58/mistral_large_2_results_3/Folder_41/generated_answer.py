import numpy as np

def submatrix_with_n_numbers(matrix, n=73):

    def count_submatrices(r, c):
        count = 0
        for i in range(r):
            for j in range(c):
                for k in range(i, r):
                    for l in range(j, c):
                        if (k - i + 1) * (l - j + 1) == n:
                            count += 1
        return count
    rows, cols = matrix.shape
    return count_submatrices(rows, cols)