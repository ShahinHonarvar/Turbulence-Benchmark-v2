import numpy as np

def submatrix_with_n_numbers(matrix):
    count, rows, cols = (0, matrix.shape[0], matrix.shape[1])
    for i in range(rows - 5):
        for j in range(cols - 5):
            if np.sum(matrix[i:i + 6, j:j + 6]) == 39:
                count += 1
    return count