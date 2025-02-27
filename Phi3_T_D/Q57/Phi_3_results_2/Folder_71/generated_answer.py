import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for x in range(rows):
        for y in range(cols):
            for size_x in range(rows - x + 1):
                for size_y in range(cols - y + 1):
                    submatrix = matrix[x:x + size_x, y:y + size_y]
                    if submatrix.sum() == 69:
                        submatrices.append(submatrix)
    return submatrices