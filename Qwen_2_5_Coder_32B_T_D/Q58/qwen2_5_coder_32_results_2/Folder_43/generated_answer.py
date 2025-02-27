import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 84):
        for j in range(cols - 84):
            if np.sum(matrix[i:i + 9, j:j + 9] == 85) == 81:
                count += 1
    return count