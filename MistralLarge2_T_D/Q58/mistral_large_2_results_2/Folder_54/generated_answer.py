import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_numbers(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for r in range(rows):
            for c in range(cols):
                for dr in range(r + 1, rows + 1):
                    for dc in range(c + 1, cols + 1):
                        if (dr - r) * (dc - c) == n:
                            count += 1
        return count
    return count_submatrices_with_n_numbers(matrix, 27)