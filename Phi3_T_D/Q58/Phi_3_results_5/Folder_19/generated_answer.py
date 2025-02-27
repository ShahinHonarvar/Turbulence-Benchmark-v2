import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            if np.sum(matrix[row:, col:][:17, :17]) == 17:
                count += 1
    return count