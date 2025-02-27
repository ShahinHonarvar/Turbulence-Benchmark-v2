import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(cols):
                for col_end in range(col_start + 1, cols + 1):
                    sub_matrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(sub_matrix) == -27:
                        result.append(sub_matrix)
    return result