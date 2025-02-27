import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 33:
        return 0
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if i + 32 < rows and j + 32 < cols:
                count += 1
    return count