import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 96):
        for j in range(cols - 96):
            if np.sum(matrix[i:i + 97, j:j + 97] == 97) == 97 ** 2:
                count += 1
    return count