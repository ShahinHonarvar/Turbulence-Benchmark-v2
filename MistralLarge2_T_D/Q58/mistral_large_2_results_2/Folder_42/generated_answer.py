import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        if (r2 - r1 + 1) * (c2 - c1 + 1) == n:
                            count += 1
        return count
    return count_submatrices(matrix, 193)