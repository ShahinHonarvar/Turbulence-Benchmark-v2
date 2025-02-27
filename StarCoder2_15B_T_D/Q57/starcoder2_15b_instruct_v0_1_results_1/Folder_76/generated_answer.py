import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices in a given matrix whose sum equals -255.
    """
    m, n = matrix.shape
    submatrices = []
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -255:
                        submatrices.append(submatrix)
    return submatrices