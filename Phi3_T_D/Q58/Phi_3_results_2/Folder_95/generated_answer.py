import numpy as np

def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    rows, cols = matrix.shape
    count = 0
    for size in range(1, min(rows, cols) + 1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if np.sum(submatrix) == 87 * size * size:
                    count += 1
    return count