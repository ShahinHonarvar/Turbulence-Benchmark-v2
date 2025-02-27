import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 46
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for k in range(j, cols):
                    if (h - i + 1) * (k - j + 1) == n:
                        count += 1
    return count