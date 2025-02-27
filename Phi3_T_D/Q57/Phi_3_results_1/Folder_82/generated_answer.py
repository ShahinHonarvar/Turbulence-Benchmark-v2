import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r_end in range(1, rows + 1):
        for c_end in range(1, cols + 1):
            for r_start in range(rows - r_end + 1):
                for c_start in range(cols - c_end + 1):
                    submatrix = matrix[r_start:r_start + r_end, c_start:c_start + c_end]
                    if submatrix.sum() == -27:
                        result.append(submatrix)
    return result