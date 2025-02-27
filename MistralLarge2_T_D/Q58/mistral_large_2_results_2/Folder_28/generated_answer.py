import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r1 in range(rows):
        for c1 in range(cols):
            for r2 in range(r1 + 1, rows + 1):
                for c2 in range(c1 + 1, cols + 1):
                    submatrix = matrix[r1:r2, c1:c2]
                    if submatrix.size == 37:
                        count += 1
    return count