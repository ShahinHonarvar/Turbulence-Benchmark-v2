import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 13):
        for j in range(cols - 13):
            if np.sum(matrix[i:i + 14, j:j + 14]) == 146:
                count += 1
    return count