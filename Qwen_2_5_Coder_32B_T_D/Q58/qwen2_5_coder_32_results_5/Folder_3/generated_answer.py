import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_count = 54
    count = 0
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for w in range(j, cols):
                    if (h - i + 1) * (w - j + 1) == target_count:
                        count += 1
    return count