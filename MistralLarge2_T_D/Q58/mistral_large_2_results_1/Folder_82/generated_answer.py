import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    n = 99
    count = 0
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1, rows):
                for c2 in range(c1, cols):
                    if (r2 - r1 + 1) * (c2 - c1 + 1) == n:
                        submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                        if np.all(submatrix != np.array(None)):
                            count += 1
    return count