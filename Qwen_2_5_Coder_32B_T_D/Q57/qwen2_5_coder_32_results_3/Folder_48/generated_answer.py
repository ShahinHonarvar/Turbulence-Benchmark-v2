import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.sum() == -261:
                        result.append(submatrix.tolist())
    return result