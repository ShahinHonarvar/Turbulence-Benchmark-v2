import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 7 + 1):
        for j in range(cols - 7 + 1):
            if np.size(matrix[i:i + 8, j:j + 8]) == 64:
                count += 1
    return count