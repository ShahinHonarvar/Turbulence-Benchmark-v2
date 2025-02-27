import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 175
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - target_count + 1):
        for j in range(cols - target_count + 1):
            if np.sum(matrix[i:i + 1, j:j + 1] == 1) == target_count:
                count += 1
    return count