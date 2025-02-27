import numpy as np

def submatrix_with_n_numbers(matrix):
    n_numbers = 126
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows - n_numbers + 1):
        for j in range(cols - n_numbers + 1):
            submatrix = matrix[i:i + n_numbers, j:j + n_numbers]
            if submatrix.size == n_numbers:
                submatrix_count += 1
    return submatrix_count