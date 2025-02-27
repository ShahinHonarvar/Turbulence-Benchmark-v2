import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix) - 1):
        for j in range(len(matrix[0]) - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.sum() == -137:
                result.append(submatrix)
    return result