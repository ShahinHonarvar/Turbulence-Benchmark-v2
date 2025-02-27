import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            for col_start in range(cols):
                for col_end in range(col_start, cols):
                    submat = matrix[row_start:row_end + 1, col_start:col_end + 1]
                    if np.sum(submat) == 432:
                        result.append(submat)
    return result