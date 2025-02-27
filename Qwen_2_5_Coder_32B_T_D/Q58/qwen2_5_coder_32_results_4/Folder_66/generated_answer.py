import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size < 42:
        return 0
    count = 0
    rows, cols = matrix.shape
    for r in range(rows - 3, -1, -1):
        for c in range(cols - 6, -1, -1):
            if np.all(matrix[r:r + 4, c:c + 7] == 42):
                count += 1
    for r in range(rows - 6, -1, -1):
        for c in range(cols - 3, -1, -1):
            if np.all(matrix[r:r + 7, c:c + 4] == 42):
                count += 1
    return count