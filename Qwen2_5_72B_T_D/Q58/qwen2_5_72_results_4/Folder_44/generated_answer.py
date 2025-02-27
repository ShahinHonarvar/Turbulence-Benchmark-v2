import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    rows, cols = matrix.shape
    target_size = 191
    count = 0
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) == target_size:
                submatrix = matrix[i:rows - i, j:cols - j]
                if submatrix.size == target_size:
                    count += 1
    return count