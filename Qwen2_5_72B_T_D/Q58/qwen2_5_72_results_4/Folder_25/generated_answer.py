import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 66
    count = 0
    for i in range(matrix.shape[0] - 7 + 1):
        for j in range(matrix.shape[1] - 9 + 1):
            if np.sum(matrix[i:i + 7, j:j + 9] == n) == 66:
                count += 1
    return count