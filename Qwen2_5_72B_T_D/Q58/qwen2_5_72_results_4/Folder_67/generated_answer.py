import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 43
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_count:
                submatrix_count += 1
    return submatrix_count