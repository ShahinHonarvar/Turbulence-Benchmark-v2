import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 193

    def count_submatrices(r, c, n):
        if r == 0 or c == 0:
            return 0
        return matrix[r][c] + count_submatrices(r - 1, c, n) + count_submatrices(r, c - 1, n) - count_submatrices(r - 1, c - 1, n)
    total_count = 0
    for start_r in range(rows):
        for start_c in range(cols):
            for end_r in range(start_r, rows):
                for end_c in range(start_c, cols):
                    if (end_r - start_r + 1) * (end_c - start_c + 1) == n:
                        if count_submatrices(end_r, end_c, n) == n:
                            total_count += 1
    return total_count