import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 16):
        for j in range(cols - 16):
            if np.sum(matrix[i:i + 15, j:j + 15]) == 175:
                count += 1
    return count