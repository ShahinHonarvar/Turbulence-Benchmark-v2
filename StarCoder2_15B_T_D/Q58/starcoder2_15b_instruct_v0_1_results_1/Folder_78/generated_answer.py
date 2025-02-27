import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.sum(sub_matrix) == 91:
                count += 1
    return count