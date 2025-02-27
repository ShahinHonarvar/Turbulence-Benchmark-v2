import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []
    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    if np.sum(matrix[top:bottom + 1, left:right + 1]) == 56:
                        submatrices.append(matrix[top:bottom + 1, left:right + 1])
    return submatrices