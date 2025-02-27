import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        return 0
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            size = min(rows - i, cols - j)
            for k in range(size):
                if sum(sum(matrix[i:i + k + 1, j:j + k + 1])) == 27 * (k + 1) ** 2:
                    count += 1
    return count