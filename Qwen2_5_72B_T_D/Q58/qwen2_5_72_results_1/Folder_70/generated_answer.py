import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 173
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) >= n:
                for r in range(i, rows):
                    for c in range(j, cols):
                        if (r - i + 1) * (c - j + 1) == n:
                            count += 1
    return count