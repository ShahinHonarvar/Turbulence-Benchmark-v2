import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -336
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for col_start in range(cols):
            for row_count in range(1, rows - row_start + 1):
                for col_count in range(1, cols - col_start + 1):
                    submatrix = matrix[row_start:row_start + row_count, col_start:col_start + col_count]
                    if submatrix.sum() == target_sum:
                        result.append(submatrix)
    return result