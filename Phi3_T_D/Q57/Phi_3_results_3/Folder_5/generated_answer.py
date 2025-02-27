import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for row_top in range(rows):
        for row_bottom in range(row_top, rows):
            for col_left in range(cols):
                for col_right in range(col_left, cols):
                    submatrix = matrix[row_top:row_bottom + 1, col_left:col_right + 1]
                    if submatrix.sum() == -43:
                        result.append(submatrix)
    return result