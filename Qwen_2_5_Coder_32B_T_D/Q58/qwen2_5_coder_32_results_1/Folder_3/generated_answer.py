import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 54
    side = int(np.sqrt(n))
    if side * side != n:
        return 0
    for i in range(rows - side + 1):
        for j in range(cols - side + 1):
            if np.prod(matrix[i:i + side, j:j + side].shape) == n:
                count += 1
    return count