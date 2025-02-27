import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Find all submatrices of the given matrix such that the sum of all integers
    in each submatrix equals -64. If no such submatrix is found, return an empty
    list.
    """
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == -64:
                        submatrices.append(submatrix)
    return submatrices