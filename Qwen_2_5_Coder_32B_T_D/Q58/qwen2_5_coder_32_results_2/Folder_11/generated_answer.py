import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 5):
        for j in range(cols - 6):
            if np.sum(matrix[i:i + 6, j:j + 7]) == 38:
                count += 1
    return count