import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 27
    row, col = matrix.shape
    count = 0
    for i in range(row - 2):
        for j in range(col - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.count_nonzero(sub_matrix) == n:
                count += 1
    return count