import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 173
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - target_count + 1):
        for j in range(cols - target_count + 1):
            if np.sum(matrix[i:i + target_count, j:j + target_count]) == target_count:
                count += 1
    return count