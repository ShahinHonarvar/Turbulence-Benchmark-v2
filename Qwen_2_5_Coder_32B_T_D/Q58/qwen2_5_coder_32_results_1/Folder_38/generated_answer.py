import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 33):
        for j in range(cols - 33):
            if np.sum(matrix[i:i + 34, j:j + 34] == 34) == 34 * 34:
                count += 1
    return count