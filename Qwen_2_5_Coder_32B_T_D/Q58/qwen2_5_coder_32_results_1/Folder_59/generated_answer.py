import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 75):
        for j in range(cols - 75):
            if np.sum(matrix[i:i + 76, j:j + 76] == 76) == 76:
                count += 1
    return count