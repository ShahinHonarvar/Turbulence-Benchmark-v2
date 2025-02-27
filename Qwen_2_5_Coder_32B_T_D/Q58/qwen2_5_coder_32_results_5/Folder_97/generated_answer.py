import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 11):
        for j in range(cols - 9):
            if np.prod(matrix[i:i + 12, j:j + 10].shape) == 120:
                count += 1
    return count