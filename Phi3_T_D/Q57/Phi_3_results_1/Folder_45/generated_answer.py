import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for left in range(cols):
        for up in range(rows):
            for right in range(left + 1, cols + 1):
                for down in range(up + 1, rows + 1):
                    submatrix = matrix[up:down, left:right]
                    if submatrix.sum() == -77:
                        result.append(submatrix)
    return result