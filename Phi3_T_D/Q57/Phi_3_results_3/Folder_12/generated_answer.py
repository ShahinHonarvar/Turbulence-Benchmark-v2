import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -83
    rows, cols = matrix.shape
    result = []
    for rowStart in range(rows):
        for colStart in range(cols):
            for rowEnd in range(rowStart, rows):
                for colEnd in range(colStart, cols):
                    submatrix = matrix[rowStart:rowEnd + 1, colStart:colEnd + 1]
                    if np.sum(submatrix) == target_sum:
                        result.append(submatrix)
    return result