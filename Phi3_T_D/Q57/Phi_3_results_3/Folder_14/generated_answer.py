import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for width in range(1, cols - j + 1):
                for height in range(1, rows - i + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if submatrix.sum() == -93:
                        result.append(submatrix)
    return result