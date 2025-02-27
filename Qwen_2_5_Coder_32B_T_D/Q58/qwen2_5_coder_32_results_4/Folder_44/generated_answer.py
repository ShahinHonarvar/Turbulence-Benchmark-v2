import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 18 + 1):
        for j in range(cols - 18 + 1):
            if np.sum(matrix[i:i + 19, j:j + 19]) == 191:
                count += 1
    return count