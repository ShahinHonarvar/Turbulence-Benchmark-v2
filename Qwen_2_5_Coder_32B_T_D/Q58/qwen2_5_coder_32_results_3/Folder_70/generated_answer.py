import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target = 173
    rows, cols = matrix.shape
    for i in range(rows - target + 1):
        for j in range(cols - target + 1):
            if np.count_nonzero(matrix[i:i + target, j:j + target] == 173) == target * target:
                count += 1
    return count