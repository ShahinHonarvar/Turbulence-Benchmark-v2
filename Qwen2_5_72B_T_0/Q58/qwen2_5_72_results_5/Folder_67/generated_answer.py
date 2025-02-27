import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 43
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_count:
                count += 1
    return count