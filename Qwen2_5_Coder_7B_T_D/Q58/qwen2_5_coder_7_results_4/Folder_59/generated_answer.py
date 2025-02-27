import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 76, rows + 1):
                for l in range(j + 76, cols + 1):
                    if (k - i) * (l - j) == 76:
                        count += 1
    return count