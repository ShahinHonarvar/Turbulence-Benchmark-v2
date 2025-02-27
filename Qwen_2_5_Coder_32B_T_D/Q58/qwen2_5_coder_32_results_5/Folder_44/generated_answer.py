import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 189):
        for j in range(cols - 189):
            if np.sum(matrix[i:i + 191, j:j + 191]) == 191:
                count += 1
    return count