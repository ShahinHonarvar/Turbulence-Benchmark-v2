import numpy as np

def submatrix_with_n_numbers(matrix):
    target_number = 99
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_number:
                submatrix_count += 1
    return submatrix_count if submatrix_count > 0 else 0