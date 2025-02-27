import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for size in range(1, rows + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == 173 * size ** 2:
                    count += 1
    return count