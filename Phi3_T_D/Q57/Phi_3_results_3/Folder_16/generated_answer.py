import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start, rows):
                for c_end in range(c_start, cols):
                    submatrix = matrix[r_start:r_end + 1, c_start:c_end + 1]
                    if submatrix.sum() == -157:
                        result.append(submatrix)
    return result