import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for left in range(cols):
        for top in range(rows):
            for width in range(1, cols - left + 1):
                for height in range(1, rows - top + 1):
                    submatrix = matrix[top:top + height, left:left + width]
                    if submatrix.sum() == -44:
                        result.append(submatrix)
    return result