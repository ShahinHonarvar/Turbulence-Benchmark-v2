import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals 997.
    """
    submatrices = []
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[0]) - 2):
            submatrix = np.array([[matrix[i][j], matrix[i][j + 1], matrix[i][j + 2]], [matrix[i + 1][j], matrix[i + 1][j + 1], matrix[i + 1][j + 2]], [matrix[i + 2][j], matrix[i + 2][j + 1], matrix[i + 2][j + 2]]])
            if submatrix.sum() == 997:
                submatrices.append(submatrix)
    return submatrices