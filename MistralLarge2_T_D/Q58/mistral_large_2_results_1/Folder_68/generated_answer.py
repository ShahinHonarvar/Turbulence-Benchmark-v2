import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 74
    count = 0

    def is_submatrix_with_n_numbers(submatrix):
        return np.count_nonzero(submatrix) == n
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r, rows):
                for c2 in range(c, cols):
                    submatrix = matrix[r:r2 + 1, c:c2 + 1]
                    if is_submatrix_with_n_numbers(submatrix):
                        count += 1
    return count