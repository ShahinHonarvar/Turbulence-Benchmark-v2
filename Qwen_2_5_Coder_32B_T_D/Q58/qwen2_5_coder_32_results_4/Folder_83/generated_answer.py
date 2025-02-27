import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 46):
        for j in range(cols - 46):
            if np.sum(matrix[i:i + 47, j:j + 47] == 47) == 47 * 47:
                count += 1
    return count