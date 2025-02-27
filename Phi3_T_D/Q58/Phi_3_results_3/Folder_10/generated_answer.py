import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(rows - i + 1):
                for l in range(cols - j + 1):
                    if k * l == 56:
                        count += 1
    return count