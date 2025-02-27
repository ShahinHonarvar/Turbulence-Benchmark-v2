import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Find all submatrices of the given matrix such that the sum of all integers in each submatrix equals -57.
    """
    submatrices = []
    for row_start in range(matrix.shape[0]):
        for row_end in range(row_start + 1, matrix.shape[0] + 1):
            for col_start in range(matrix.shape[1]):
                for col_end in range(col_start + 1, matrix.shape[1] + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == -57:
                        submatrices.append(submatrix)
    return submatrices