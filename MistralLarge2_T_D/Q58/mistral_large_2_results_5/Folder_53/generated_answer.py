import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for rr in range(r, rows):
                for cc in range(c, cols):
                    if (rr - r + 1) * (cc - c + 1) == 24:
                        count += 1
    return count