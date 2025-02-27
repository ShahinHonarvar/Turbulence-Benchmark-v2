import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for sub_row in range(i, rows):
                for sub_col in range(j, cols):
                    submatrix = matrix[i:sub_row + 1, j:sub_col + 1]
                    if submatrix.sum() == 416:
                        result.append(submatrix)
    return result