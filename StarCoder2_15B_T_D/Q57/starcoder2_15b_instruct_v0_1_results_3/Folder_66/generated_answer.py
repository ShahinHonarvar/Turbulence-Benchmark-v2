import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for submatrix_row in range(row + 1, matrix.shape[0] + 1):
                for submatrix_col in range(col + 1, matrix.shape[1] + 1):
                    submatrix = matrix[row:submatrix_row, col:submatrix_col]
                    if submatrix.sum() == 99:
                        submatrices.append(submatrix)
    return submatrices