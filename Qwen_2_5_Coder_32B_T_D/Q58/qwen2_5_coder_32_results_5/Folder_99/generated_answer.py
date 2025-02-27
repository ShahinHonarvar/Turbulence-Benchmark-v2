import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_count, col_count = matrix.shape
    for i in range(row_count - 13):
        for j in range(col_count - 13):
            if np.sum(matrix[i:i + 14, j:j + 14]) == 146:
                count += 1
    return count