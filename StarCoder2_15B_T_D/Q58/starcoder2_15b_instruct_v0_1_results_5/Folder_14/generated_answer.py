import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row - 2):
        for j in range(col - 2):
            sub_matrix = matrix[i:i + 3, j:j + 3]
            if np.sum(sub_matrix) == 84:
                count += 1
    return count