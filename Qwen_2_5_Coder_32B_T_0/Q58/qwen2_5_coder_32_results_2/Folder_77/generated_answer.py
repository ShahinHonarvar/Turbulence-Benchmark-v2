import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 168):
        for j in range(cols - 168):
            if np.sum(matrix[i:i + 179, j:j + 179]) == 179:
                count += 1
    return count