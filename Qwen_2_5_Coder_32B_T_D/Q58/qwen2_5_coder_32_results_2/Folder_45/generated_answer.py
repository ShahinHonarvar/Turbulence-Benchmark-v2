import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 4 + 1):
        for j in range(cols - 4 + 1):
            if np.sum(matrix[i:i + 4, j:j + 4]) == 28:
                count += 1
    return count