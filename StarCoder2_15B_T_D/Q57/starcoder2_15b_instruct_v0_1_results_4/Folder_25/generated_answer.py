import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals -20.
    """
    submatrices = []
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            for submatrix_size in range(1, min(len(matrix) - row, len(matrix[0]) - column) + 1):
                submatrix = matrix[row:row + submatrix_size, column:column + submatrix_size]
                if np.sum(submatrix) == -20:
                    submatrices.append(submatrix)
    return submatrices