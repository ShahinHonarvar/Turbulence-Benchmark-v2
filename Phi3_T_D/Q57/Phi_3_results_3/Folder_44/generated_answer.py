import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sum_target = 830
    submatrices = []
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i + 1, cols - j + 1) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.sum() == sum_target:
                    submatrices.append(submatrix)
    return submatrices