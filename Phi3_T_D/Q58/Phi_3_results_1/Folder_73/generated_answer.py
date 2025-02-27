import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    def count_submatrix(r1, c1, r2, c2):
        return np.sum(np.ones((r2 - r1 + 1, c2 - c1 + 1), dtype=int))
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if count_submatrix(r1, c1, r2, c2) == 41:
                        count += 1
    return count