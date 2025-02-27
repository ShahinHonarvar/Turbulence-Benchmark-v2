import numpy as np

def submatrix_with_particular_sum(matrix):
    result_submatrices = []
    rows, cols = matrix.shape
    target_sum = -394
    for i in range(rows):
        for j in range(cols):
            for m in range(1, rows - i + 1):
                for n in range(1, cols - j + 1):
                    submatrix = matrix[i:i + m, j:j + n]
                    if submatrix.sum() == target_sum:
                        result_submatrices.append(submatrix)
    return result_submatrices