import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 95
    count = 0
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            sub_matrix = matrix[i:i + n, j:j + n]
            if np.sum(sub_matrix) == 95:
                count += 1
    return count