import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_end in range(r, rows):
                for c_end in range(c, cols):
                    submatrix = matrix[r:r_end + 1, c:c_end + 1]
                    if submatrix.size == 154:
                        count += 1
    return count