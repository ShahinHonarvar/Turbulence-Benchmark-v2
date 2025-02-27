import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 56
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i, rows):
                for c in range(j, cols):
                    if (r - i + 1) * (c - j + 1) == target_size:
                        count += 1
    return count