import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 91
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows - 9):
        for j in range(cols - 9):
            if np.sum(matrix[i:i + 10, j:j + 10] == target_count) == target_count:
                submatrix_count += 1
    return submatrix_count