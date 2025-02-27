import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = int(np.sqrt(72))
    if target_size ** 2 != 72:
        return 0
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - target_size + 1):
        for j in range(cols - target_size + 1):
            if np.sum(matrix[i:i + target_size, j:j + target_size]) == 72:
                count += 1
    return count