import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for width in range(1, rows - x + 1):
                for height in range(1, cols - y + 1):
                    submatrix = matrix[x:x + width, y:y + height]
                    if submatrix.sum() == 8:
                        submatrices.append(submatrix)
    return submatrices