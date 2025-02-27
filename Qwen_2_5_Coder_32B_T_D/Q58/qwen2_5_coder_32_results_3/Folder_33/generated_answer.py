import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 10 + 1):
        for j in range(cols - 10 + 1):
            if np.sum(matrix[i:i + 10, j:j + 10]) == 118:
                count += 1
    return count