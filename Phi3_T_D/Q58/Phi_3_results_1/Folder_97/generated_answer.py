import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 11):
        for j in range(matrix.shape[1] - 11):
            if np.all(matrix[i:i + 12, j:j + 12]):
                count += 1
    return count