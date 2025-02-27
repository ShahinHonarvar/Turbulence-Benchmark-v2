import numpy as np

def submatrix_with_particular_sum(matrix):
    min_dim = min(matrix.shape)
    result = []
    for size in range(1, min_dim + 1):
        for row in range(matrix.shape[0] - size + 1):
            for col in range(matrix.shape[1] - size + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if submatrix.sum() == -42:
                    result.append(submatrix)
    return result