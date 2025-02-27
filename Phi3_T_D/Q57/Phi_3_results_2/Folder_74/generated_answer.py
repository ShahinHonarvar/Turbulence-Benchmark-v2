import numpy as np

def submatrix_with_particular_sum(matrix, target_sum=88):
    submatrices = []
    rows, cols = matrix.shape
    for left in range(cols):
        for top in range(rows):
            for right in range(left, cols):
                for bottom in range(top, rows):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix.tolist())
    return submatrices