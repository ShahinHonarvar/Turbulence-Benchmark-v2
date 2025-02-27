import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    target_size = 60
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if (i + 1) * (j + 1) == target_size:
                count += 1
    return count