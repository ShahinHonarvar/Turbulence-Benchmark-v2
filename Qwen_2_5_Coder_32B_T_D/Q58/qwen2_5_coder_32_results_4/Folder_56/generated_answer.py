import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 5):
        for j in range(cols - 5):
            if np.sum(matrix[i:i + 6, j:j + 6]) == 68:
                count += 1
    return count