import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    shape = matrix.shape
    for i in range(shape[0] - 13):
        for j in range(shape[1] - 13):
            if np.sum(matrix[i:i + 14, j:j + 14]) == 147:
                count += 1
    return count