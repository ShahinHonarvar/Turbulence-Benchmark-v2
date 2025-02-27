import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    target_sum = 34
    for left in range(cols):
        for right in range(left, cols):
            for top in range(rows):
                for bottom in range(top, rows):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if np.sum(submatrix) == target_sum:
                        submatrices.append(submatrix)
    return submatrices