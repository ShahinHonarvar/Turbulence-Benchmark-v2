import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 179

    def count_submatrices(r, c):
        total = 0
        for i in range(r):
            for j in range(c):
                if (i + 1) * (j + 1) == target_size:
                    total += (rows - i) * (cols - j)
        return total
    return count_submatrices(rows, cols)