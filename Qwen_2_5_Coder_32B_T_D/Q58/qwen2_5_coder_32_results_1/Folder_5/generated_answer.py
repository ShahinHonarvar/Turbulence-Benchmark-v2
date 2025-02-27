import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 63
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 7 + 1):
        for j in range(cols - 7 + 1):
            if np.sum(matrix[i:i + 7, j:j + 7]) == target_count:
                count += 1
    return count