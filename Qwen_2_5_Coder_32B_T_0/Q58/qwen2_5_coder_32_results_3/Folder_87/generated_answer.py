import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 95):
        for j in range(cols - 95):
            if np.size(matrix[i:i + 96, j:j + 96]) == 96:
                count += 1
    return count