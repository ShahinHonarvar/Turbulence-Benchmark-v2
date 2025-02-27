import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 62):
        for j in range(cols - 62):
            if np.sum(matrix[i:i + 7, j:j + 7] == 63) == 63:
                count += 1
    return count