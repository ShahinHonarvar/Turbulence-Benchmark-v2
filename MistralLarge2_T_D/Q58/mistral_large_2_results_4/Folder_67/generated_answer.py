import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def is_valid_submatrix(r, c, size):
        if r + size > rows or c + size > cols:
            return False
        return np.count_nonzero(matrix[r:r + size, c:c + size]) == 43
    for r in range(rows):
        for c in range(cols):
            for size in range(1, min(rows - r, cols - c) + 1):
                if is_valid_submatrix(r, c, size):
                    count += 1
    return count