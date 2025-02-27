import numpy as np

def submatrix_with_n_numbers(matrix):
    target = 80
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 7):
        for j in range(cols - 7):
            if np.sum(matrix[i:i + 8, j:j + 8]) == target:
                count += 1
    return count