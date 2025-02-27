import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    submatrix_size = 121
    rows, cols = matrix.shape
    for i in range(rows - 10 + 1):
        for j in range(cols - 10 + 1):
            submatrix = matrix[i:i + 11, j:j + 11]
            if submatrix.size == submatrix_size:
                count += 1
    return count