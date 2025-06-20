import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 11):
        for j in range(cols - 11):
            if np.sum(matrix[i:i + 12, j:j + 12] == 127) == 144:
                count += 1
    return count