import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    target_size = 130
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            submatrix = matrix[i:rows, j:cols]
            if submatrix.size == target_size:
                count += 1
    return count