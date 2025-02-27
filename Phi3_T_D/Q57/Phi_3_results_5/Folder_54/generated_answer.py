import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i + 1, cols - j + 1)):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.sum() == -59:
                    result.append(submatrix)
    return result