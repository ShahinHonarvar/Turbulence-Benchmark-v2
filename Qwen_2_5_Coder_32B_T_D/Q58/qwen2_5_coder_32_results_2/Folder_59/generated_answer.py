import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 76
    count = 0
    for i in range(rows - target_size + 1):
        for j in range(cols - target_size + 1):
            if np.size(matrix[i:i + target_size, j:j + target_size]) == target_size:
                count += 1
    return count