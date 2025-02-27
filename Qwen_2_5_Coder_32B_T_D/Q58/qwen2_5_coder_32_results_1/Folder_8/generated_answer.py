import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 28):
        for j in range(cols - 28):
            if np.sum(matrix[i:i + 5, j:j + 5]) == 29:
                count += 1
    return count