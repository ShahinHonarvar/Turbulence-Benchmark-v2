import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows, 1):
                for l in range(j, cols, 1):
                    if (k - i + 1) * (l - j + 1) == 19:
                        count += 1
    return count