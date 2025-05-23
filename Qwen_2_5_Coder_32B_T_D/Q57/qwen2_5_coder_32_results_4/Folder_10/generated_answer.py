import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    submatrix = matrix[i:r, j:c]
                    if submatrix.sum() == 56:
                        result.append(submatrix)
    return result