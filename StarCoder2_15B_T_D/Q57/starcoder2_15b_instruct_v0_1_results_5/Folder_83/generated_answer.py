import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for submatrix_row in range(row, matrix.shape[0]):
                for submatrix_col in range(col, matrix.shape[1]):
                    submatrix = matrix[row:submatrix_row + 1, col:submatrix_col + 1]
                    if np.sum(submatrix) == -15:
                        submatrices.append(submatrix)
    return submatrices