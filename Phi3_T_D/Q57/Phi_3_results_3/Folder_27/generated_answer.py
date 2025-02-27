import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    found_submatrices = []
    for rowStart in range(rows):
        for rowEnd in range(rowStart, rows):
            for colStart in range(cols):
                for colEnd in range(colStart, cols):
                    submatrix = matrix[rowStart:rowEnd + 1, colStart:colEnd + 1]
                    if np.sum(submatrix) == 77:
                        found_submatrices.append(submatrix)
    return found_submatrices