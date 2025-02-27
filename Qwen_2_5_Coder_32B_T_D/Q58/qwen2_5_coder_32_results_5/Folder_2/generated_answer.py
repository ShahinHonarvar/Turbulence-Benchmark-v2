import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    required_size = 107
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    if (m - i + 1) * (n - j + 1) == required_size:
                        count += 1
    return count