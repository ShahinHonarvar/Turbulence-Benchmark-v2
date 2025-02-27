import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    if rows * cols < 51:
        return 0
    for i in range(rows - 7):
        for j in range(cols - 7):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == 51:
                count += 1
    return count