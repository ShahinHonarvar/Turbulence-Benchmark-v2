import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 3):
        for j in range(cols - 3):
            if np.size(matrix[i:i + 4, j:j + 4]) == 19:
                count += 1
    return count