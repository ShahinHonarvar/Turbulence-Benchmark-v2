import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 191
    rows, cols = matrix.shape
    if rows * cols < n:
        return 0
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) >= n:
                for x in range(i, rows):
                    for y in range(j, cols):
                        if (x - i + 1) * (y - j + 1) == n:
                            count += 1
    return count