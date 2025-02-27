import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 3):
        for j in range(cols - 3):
            if np.array_equal(matrix[i:i + 4, j:j + 4].flatten(), np.array([4] * 16)):
                count += 1
    return count