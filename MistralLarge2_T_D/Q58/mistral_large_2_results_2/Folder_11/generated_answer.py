import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r, rows):
                for c2 in range(c, cols):
                    if (r2 - r + 1) * (c2 - c + 1) == 38:
                        count += 1
    return count