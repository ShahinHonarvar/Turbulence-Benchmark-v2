import numpy as np

def submatrix_with_particular_sum(matrix):
    height, width = matrix.shape
    result = []
    for i in range(height):
        for j in range(width):
            for k in range(i, height):
                for l in range(j, width):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -47:
                        result.append(submatrix)
    return result