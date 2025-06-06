import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 16):
        for j in range(cols - 16):
            if np.sum(matrix[i:i + 16, j:j + 16]) == 176:
                count += 1
    return count