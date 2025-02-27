import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r0 in range(rows):
        for r1 in range(r0, rows):
            for c0 in range(cols):
                for c1 in range(c0, cols):
                    if (r1 - r0 - 1) * (c1 - c0 - 1) == 3:
                        count += 1
    return count