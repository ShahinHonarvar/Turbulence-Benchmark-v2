import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    height, width = matrix.shape
    count = 0
    n = 51
    for i in range(height):
        for j in range(width):
            if i + n <= height and j + n <= width:
                count += 1
    return count