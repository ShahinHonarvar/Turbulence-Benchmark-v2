import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 13):
        for j in range(col - 13):
            sub_matrix = matrix[i:i + 14, j:j + 14]
            if np.sum(sub_matrix) == 144:
                count += 1
    return count