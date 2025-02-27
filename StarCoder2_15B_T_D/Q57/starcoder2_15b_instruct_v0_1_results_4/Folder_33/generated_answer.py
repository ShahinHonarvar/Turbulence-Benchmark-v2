import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Find all submatrices in `matrix` whose sum is -811.
    """
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -811:
                        submatrices.append(submatrix)
    return submatrices