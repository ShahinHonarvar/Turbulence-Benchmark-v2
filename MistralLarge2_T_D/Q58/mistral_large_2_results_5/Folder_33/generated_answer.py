import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r2 in range(r, rows):
                for c2 in range(c, cols):
                    submatrix = matrix[r:r2 + 1, c:c2 + 1]
                    if submatrix.size == 118:
                        count += 1
    return count