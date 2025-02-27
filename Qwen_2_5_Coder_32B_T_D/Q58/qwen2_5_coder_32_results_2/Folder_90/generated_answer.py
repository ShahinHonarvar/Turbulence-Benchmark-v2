import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 176
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if (m - i + 1) * (n - j + 1) == target_size:
                        count += 1
    return count