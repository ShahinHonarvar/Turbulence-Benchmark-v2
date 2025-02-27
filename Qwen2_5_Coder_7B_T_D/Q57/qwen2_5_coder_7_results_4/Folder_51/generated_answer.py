import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            submatrix_sum = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix_sum += matrix[k, l]
                    if submatrix_sum == -46:
                        result.append(matrix[i:k + 1, j:l + 1])
    return result