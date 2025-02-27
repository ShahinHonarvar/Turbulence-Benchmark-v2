import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target = 85
    for i in range(rows - target + 1):
        for j in range(cols - target + 1):
            if np.sum(matrix[i:i + target, j:j + target]) == target:
                count += 1
    return count