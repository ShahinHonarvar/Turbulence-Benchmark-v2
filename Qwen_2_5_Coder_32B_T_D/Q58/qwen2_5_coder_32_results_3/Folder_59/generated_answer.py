import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 6):
        for j in range(cols - 6):
            if np.sum(matrix[i:i + 8, j:j + 8] == 76) == 76:
                count += 1
    return count