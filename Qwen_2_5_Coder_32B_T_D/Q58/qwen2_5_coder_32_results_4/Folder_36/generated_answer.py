import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 12):
        for j in range(cols - 12):
            if np.sum(matrix[i:i + 13, j:j + 13]) == 131:
                count += 1
    return count