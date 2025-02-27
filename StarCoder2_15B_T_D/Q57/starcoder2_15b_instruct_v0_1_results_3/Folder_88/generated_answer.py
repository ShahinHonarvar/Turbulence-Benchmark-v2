import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            for submatrix_row in range(row + 1, len(matrix) + 1):
                for submatrix_column in range(column + 1, len(matrix[row]) + 1):
                    submatrix = matrix[row:submatrix_row, column:submatrix_column]
                    if np.sum(submatrix) == -64:
                        submatrices.append(submatrix)
    return submatrices