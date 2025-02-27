import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 11):
        for j in range(cols - 11):
            if np.prod(matrix[i:i + 12, j:j + 12].shape) == 144:
                count += 1
    return count