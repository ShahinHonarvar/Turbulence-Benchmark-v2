import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for sub_row in range(i + 1, rows + 1):
                for sub_col in range(j + 1, cols + 1):
                    if matrix[i:sub_row, j:sub_col].sum() == -9:
                        result.append(matrix[i:sub_row, j:sub_col])
    return result