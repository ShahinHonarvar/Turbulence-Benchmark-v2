import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    submat = matrix[i:m + 1, j:n + 1]
                    if submat.sum() == -3:
                        result.append(submat)
    return result