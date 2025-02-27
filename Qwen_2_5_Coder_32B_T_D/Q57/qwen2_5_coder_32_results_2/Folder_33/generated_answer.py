import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for sub_row in range(i + 1, rows + 1):
                for sub_col in range(j + 1, cols + 1):
                    submatrix = matrix[i:sub_row, j:sub_col]
                    if np.sum(submatrix) == -811:
                        result.append(submatrix)
    return result