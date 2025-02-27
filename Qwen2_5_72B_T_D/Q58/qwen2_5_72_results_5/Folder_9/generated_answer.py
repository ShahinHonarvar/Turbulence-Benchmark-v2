import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 5 + 1):
        for j in range(cols - 11 + 1):
            if np.sum(matrix[i:i + 5, j:j + 11].size == 33):
                count += 1
    return count