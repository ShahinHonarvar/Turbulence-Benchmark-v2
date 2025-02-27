import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.size == 0:
        return []
    rows, cols = matrix.shape
    submatrices = []
    for rowStart in range(1, rows):
        for rowEnd in range(rowStart, rows):
            row_sum = np.sum(matrix[rowStart:rowEnd + 1], axis=0)
            if not (row_sum >= 100).all():
                continue
            for colStart in range(1, cols):
                for colEnd in range(colStart, cols):
                    col_sum = np.sum(matrix[rowStart:rowEnd + 1, colStart:colEnd + 1])
                    if col_sum == 100:
                        submatrices.append(matrix[rowStart:rowEnd + 1, colStart:colEnd + 1])
    return submatrices