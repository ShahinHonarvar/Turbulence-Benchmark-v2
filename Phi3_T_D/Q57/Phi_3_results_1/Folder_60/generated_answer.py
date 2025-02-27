import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sum_target = 94
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            current_sum = 0
            for row in range(i, rows):
                for col in range(j, cols):
                    current_sum += matrix[row][col]
                    submatrix = matrix[i:row + 1, j:col + 1]
                    if current_sum == sum_target:
                        submatrices.append(submatrix)
    return submatrices