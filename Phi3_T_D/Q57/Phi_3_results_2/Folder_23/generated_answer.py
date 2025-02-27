import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for top_left_row in range(rows):
        for top_left_col in range(cols):
            for size_row in range(1, rows - top_left_row + 1):
                for size_col in range(1, cols - top_left_col + 1):
                    submatrix = matrix[top_left_row:top_left_row + size_row, top_left_col:top_left_col + size_col]
                    if submatrix.sum() == 59:
                        result.append(submatrix)
    return result