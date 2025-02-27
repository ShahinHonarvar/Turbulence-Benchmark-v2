import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_submatrix_sum(x1, y1, x2, y2):
        return matrix[x1:x2 + 1, y1:y2 + 1].sum()
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if get_submatrix_sum(x1, y1, x2, y2) == -93:
                        result.append(matrix[x1:x2 + 1, y1:y2 + 1])
    return result