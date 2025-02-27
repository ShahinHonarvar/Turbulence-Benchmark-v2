import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_size = 130 ** 0.5
    if not target_size.is_integer():
        return 0
    target_size = int(target_size)
    for i in range(rows - target_size + 1):
        for j in range(cols - target_size + 1):
            if np.sum(matrix[i:i + target_size, j:j + target_size]) == 130:
                count += 1
    return count