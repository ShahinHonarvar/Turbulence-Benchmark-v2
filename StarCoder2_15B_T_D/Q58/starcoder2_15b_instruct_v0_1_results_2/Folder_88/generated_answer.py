import numpy as np

def submatrix_with_n_numbers(matrix):
    n, m = matrix.shape
    count = 0
    for i in range(n - 2):
        for j in range(m - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.sum(sub_matrix) == 67:
                count += 1
    return count