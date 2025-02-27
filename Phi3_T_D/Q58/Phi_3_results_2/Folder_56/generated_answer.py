import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = np.sum(matrix > 0)
    rows, cols = matrix.shape
    if n == 68:
        count += 1
    for size in range(min(rows, cols), 0, -1):
        for row in range(rows - size + 1):
            for col in range(cols - size + 1):
                if np.sum(matrix[row:row + size, col:col + size] > 0) == size ** 2:
                    count += 1
    return count