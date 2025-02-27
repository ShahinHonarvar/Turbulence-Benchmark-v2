import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 6 + 1):
        for j in range(cols - 6 + 1):
            if np.count_nonzero(matrix[i:i + 6, j:j + 6]) == 48:
                count += 1
    return count