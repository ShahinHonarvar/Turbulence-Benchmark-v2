import numpy as np

def submatrix_with_particular_sum(matrix, target_sum=126):
    submatrices = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.sum() == target_sum:
                    submatrices.append(submatrix)
    return submatrices