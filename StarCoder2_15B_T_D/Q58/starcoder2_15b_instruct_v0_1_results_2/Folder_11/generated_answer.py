import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            sub_matrix = matrix[i:i + 2, j:j + 2]
            if np.sum(sub_matrix) == 38:
                count += 1
    return count