import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(i + 1, rows + 1):
                for sub_cols in range(j + 1, cols + 1):
                    submatrix = matrix[i:sub_rows, j:sub_cols]
                    if np.sum(submatrix) == -86:
                        submatrices.append(submatrix)
    return submatrices