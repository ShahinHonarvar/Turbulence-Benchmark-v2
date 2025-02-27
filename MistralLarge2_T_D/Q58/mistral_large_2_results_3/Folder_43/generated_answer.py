import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 85
    count = 0

    def count_elements(submatrix):
        return np.sum(submatrix != 0)
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if count_elements(submatrix) == n:
                        count += 1
    return count