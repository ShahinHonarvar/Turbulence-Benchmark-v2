import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start + 1, rows + 1):
                for c_end in range(c_start + 1, cols + 1):
                    submatrix = matrix[r_start:r_end, c_start:c_end]
                    if submatrix.size == 48:
                        count += 1
    return count