import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    n = 173
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for k in range(j, cols):
                    if (m - i + 1) * (k - j + 1) == n:
                        count += 1
    return count