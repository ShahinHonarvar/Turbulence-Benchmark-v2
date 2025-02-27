import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for a in range(i, rows):
                for b in range(j, cols):
                    submatrix_size = (a - i + 1) * (b - j + 1)
                    if submatrix_size == 56:
                        count += 1
    return count