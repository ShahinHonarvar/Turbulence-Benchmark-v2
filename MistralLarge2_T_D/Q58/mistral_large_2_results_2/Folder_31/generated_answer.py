import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 45
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r, rows):
                for c_end in range(c, cols):
                    if (r_end - r + 1) * (c_end - c + 1) == n:
                        count += 1
    return count