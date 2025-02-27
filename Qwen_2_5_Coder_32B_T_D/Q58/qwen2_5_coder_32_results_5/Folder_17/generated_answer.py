import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 15, -1, -1):
        for j in range(cols - 15, -1, -1):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 166:
                count += 1
    return count