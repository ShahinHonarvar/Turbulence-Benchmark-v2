import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 103

    def count_submatrices(r, c):
        if r < 0 or c < 0:
            return 0
        return prefix_sum[r, c] - (prefix_sum[r - 1, c] if r > 0 else 0) - (prefix_sum[r, c - 1] if c > 0 else 0) + (prefix_sum[r - 1, c - 1] if r > 0 and c > 0 else 0)
    prefix_sum = np.zeros((rows + 1, cols + 1), dtype=int)
    for r in range(rows):
        for c in range(cols):
            prefix_sum[r + 1, c + 1] = prefix_sum[r, c + 1] + prefix_sum[r + 1, c] - prefix_sum[r, c] + matrix[r, c]
    count = 0
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if count_submatrices(r2, c2) - count_submatrices(r1 - 1, c2) - count_submatrices(r2, c1 - 1) + count_submatrices(r1 - 1, c1 - 1) == n:
                        count += 1
    return count