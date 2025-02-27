import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for left in range(cols):
        for top in range(rows):
            for right in range(left + 1, cols + 1):
                for bottom in range(top + 1, rows + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.sum() == 15:
                        result.append(submatrix)
    return result