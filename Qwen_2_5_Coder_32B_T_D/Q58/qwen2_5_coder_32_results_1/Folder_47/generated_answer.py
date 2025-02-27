import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    r, c = matrix.shape
    for i in range(r - 8):
        for j in range(c - 8):
            if np.sum(matrix[i:i + 9, j:j + 9]) == 90:
                count += 1
    return count