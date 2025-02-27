import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    for top in range(matrix.shape[0]):
        for left in range(matrix.shape[1]):
            for bottom in range(top + 1, matrix.shape[0] + 1):
                for right in range(left + 1, matrix.shape[1] + 1):
                    submatrix = matrix[top:bottom, left:right]
                    if submatrix.sum() == 56:
                        submatrices.append(submatrix)
    return submatrices