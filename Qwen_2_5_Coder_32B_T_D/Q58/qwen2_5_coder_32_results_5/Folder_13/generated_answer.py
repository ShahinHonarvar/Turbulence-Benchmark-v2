import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 175
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if (k - i + 1) * (l - j + 1) == n:
                        count += 1
    return count