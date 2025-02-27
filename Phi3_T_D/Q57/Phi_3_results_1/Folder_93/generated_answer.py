import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    sub_matrix = matrix[i:x + 1, j:y + 1]
                    if sub_matrix.sum() == -65:
                        result.append(sub_matrix)
    return result