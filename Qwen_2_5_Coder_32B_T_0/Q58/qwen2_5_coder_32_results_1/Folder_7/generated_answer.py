import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 10):
        for j in range(cols - 10):
            if np.sum(matrix[i:i + 11, j:j + 11]) == 121:
                count += 1
    return count