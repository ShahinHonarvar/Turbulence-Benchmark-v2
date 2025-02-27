import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []
    for i in range(m):
        for j in range(n):
            for height in range(1, m - i + 1):
                for width in range(1, n - j + 1):
                    submatrix = matrix[i:i + height, j:j + width]
                    if submatrix.sum() == -63:
                        result.append(submatrix)
    return result