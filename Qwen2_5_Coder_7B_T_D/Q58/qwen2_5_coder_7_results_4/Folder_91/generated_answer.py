import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 4):
        for j in range(cols - 4):
            if np.array_equal(matrix[i:i + 5, j:j + 5], np.array([[5] * 5 for _ in range(5)])):
                count += 1
    return count