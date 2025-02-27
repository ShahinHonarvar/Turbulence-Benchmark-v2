import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for row in range(len(matrix) - 1):
        for col in range(len(matrix[0]) - 1):
            submatrix = matrix[row:row + 2, col:col + 2]
            if np.sum(submatrix) == 245:
                submatrices.append(submatrix)
    return submatrices