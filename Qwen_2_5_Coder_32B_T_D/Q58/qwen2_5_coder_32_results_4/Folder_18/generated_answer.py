import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    target_size = 104
    side = int(np.sqrt(target_size))
    if side * side != target_size:
        return 0
    for i in range(rows - side + 1):
        for j in range(cols - side + 1):
            if matrix[i:i + side, j:j + side].size == target_size:
                count += 1
    return count