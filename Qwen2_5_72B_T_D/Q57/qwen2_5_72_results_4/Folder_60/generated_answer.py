import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_of_submatrix(mat, x1, y1, x2, y2):
        sum_val = 0
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                sum_val += mat[i][j]
        return sum_val
    rows, cols = matrix.shape
    result = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if sum_of_submatrix(matrix, x1, y1, x2, y2) == 94:
                        result.append(matrix[x1:x2 + 1, y1:y2 + 1])
    return result