import numpy as np

def submatrix_with_particular_sum(matrix):
    total_elements = matrix.shape[0] * matrix.shape[1]
    submatrices = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            for size_row in range(1, matrix.shape[0] - start_row + 1):
                for size_col in range(1, matrix.shape[1] - start_col + 1):
                    submatrix = matrix[start_row:start_row + size_row, start_col:start_col + size_col]
                    if submatrix.sum() == -38:
                        submatrices.append(submatrix)
    return submatrices