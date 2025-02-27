import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    current_sum = 0
                    for x in range(i, p + 1):
                        for y in range(j, q + 1):
                            current_sum += matrix[x, y]
                    if current_sum == 99:
                        submatrix = matrix[i:p + 1, j:q + 1]
                        result.append(submatrix)
    return result