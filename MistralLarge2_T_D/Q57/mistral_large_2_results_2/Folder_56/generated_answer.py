import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrices = []
    for top in range(m):
        for bottom in range(top, m):
            for left in range(n):
                for right in range(left, n):
                    submatrix = matrix[top:bottom + 1, left:right + 1]
                    if submatrix.sum() == -50:
                        submatrices.append(submatrix)
    return submatrices