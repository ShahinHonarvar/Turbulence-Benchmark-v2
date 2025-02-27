import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_number = 111
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_number:
                count += 1
    return count