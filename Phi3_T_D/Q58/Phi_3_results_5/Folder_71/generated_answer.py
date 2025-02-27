import numpy as np

def submatrix_with_n_numbers(matrix):
    row_count, col_count = matrix.shape
    count = 0
    for size in range(1, min(row_count, col_count) + 1):
        for r in range(row_count - size + 1):
            for c in range(col_count - size + 1):
                if np.sum(matrix[r:r + size, c:c + size]) == 78 * size ** 2:
                    count += 1
    return count