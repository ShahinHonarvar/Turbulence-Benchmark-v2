import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns a list of all submatrices of the given matrix such that the sum of all
    integers in each submatrix equals -10. If no such submatrix is found, returns an
    empty list.
    """
    submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for sub_row in range(row, matrix.shape[0]):
                for sub_col in range(col, matrix.shape[1]):
                    submatrix = matrix[row:sub_row + 1, col:sub_col + 1]
                    if submatrix.sum() == -10:
                        submatrices.append(submatrix)
    return submatrices