import numpy as np

def submatrix_with_particular_sum(matrix):
    result_submatrix = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submat = matrix[i:k, j:l]
                    if submat.sum() == 35:
                        result_submatrix.append(submat)
    return result_submatrix