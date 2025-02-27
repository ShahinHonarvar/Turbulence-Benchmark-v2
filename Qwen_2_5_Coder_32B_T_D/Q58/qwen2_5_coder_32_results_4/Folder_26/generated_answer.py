import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 115
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if (m - i + 1) * (n - j + 1) == target_count:
                        count += 1
    return count