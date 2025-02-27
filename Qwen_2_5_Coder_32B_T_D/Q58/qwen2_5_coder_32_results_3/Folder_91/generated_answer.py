import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return count
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.size == 5:
                count += 1
    return count