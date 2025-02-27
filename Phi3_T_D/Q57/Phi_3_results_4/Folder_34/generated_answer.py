import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for rows_count in range(i + 1, rows + 1):
                for cols_count in range(j + 1, cols + 1):
                    submatrix = matrix[i:rows_count, j:cols_count]
                    if submatrix.sum() == -13:
                        submatrices.append(submatrix)
    return submatrices