import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    h, w = matrix.shape
    for i in range(h - 4):
        for j in range(w - 4):
            if np.sum(matrix[i:i + 5, j:j + 5]) == 53:
                count += 1
    return count