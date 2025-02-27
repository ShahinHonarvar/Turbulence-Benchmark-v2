import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 103
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == n:
                count += 1
    return count