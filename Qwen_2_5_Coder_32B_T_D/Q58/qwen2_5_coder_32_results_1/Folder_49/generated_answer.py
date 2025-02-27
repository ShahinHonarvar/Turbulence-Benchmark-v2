import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    h, w = matrix.shape
    for i in range(h - 8):
        for j in range(w - 8):
            submatrix = matrix[i:i + 9, j:j + 9]
            if np.size(submatrix) == 72:
                count += 1
    return count