import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(x, y, width, height):
        return matrix[x:x + width, y:y + height].sum()
    rows, cols = matrix.shape
    result = []
    for x in range(rows):
        for y in range(cols):
            for width in range(1, rows - x + 1):
                for height in range(1, cols - y + 1):
                    if submatrix_sum(x, y, width, height) == -255:
                        result.append(matrix[x:x + width, y:y + height])
    return result