import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def is_submatrix_valid(r, c):
        if r >= rows or c >= cols:
            return False
        submatrix = matrix[r:r + 2, c:c + 3]
        return np.size(submatrix) == 6
    for r in range(rows - 1):
        for c in range(cols - 2):
            if is_submatrix_valid(r, c):
                count += 1
    return count