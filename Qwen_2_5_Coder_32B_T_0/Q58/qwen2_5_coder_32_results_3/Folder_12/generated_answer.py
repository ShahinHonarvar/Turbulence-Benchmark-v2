import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 6):
        for j in range(cols - 6):
            if np.sum(matrix[i:i + 6, j:j + 6]) == 46:
                count += 1
    return count