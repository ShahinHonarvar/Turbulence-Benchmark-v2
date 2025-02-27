import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    total_submatrices = []
    for top in range(rows):
        for left in range(cols):
            for bottom in range(top, rows):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == -38:
                        total_submatrices.append(submatrix)
    return total_submatrices