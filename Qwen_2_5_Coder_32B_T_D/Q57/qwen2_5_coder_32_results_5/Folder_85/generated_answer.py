import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for h in range(i, rows):
                for k in range(j, cols):
                    submatrix = matrix[i:h + 1, j:k + 1]
                    if submatrix.sum() == -87:
                        result.append(submatrix)
    return result