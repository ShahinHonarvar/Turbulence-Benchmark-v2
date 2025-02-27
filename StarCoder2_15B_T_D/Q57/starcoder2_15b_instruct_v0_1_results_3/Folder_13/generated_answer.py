import numpy as np

def submatrix_with_particular_sum(matrix):
    """Find all submatrices of the given matrix such that the sum of all integers in each submatrix equals 382."""
    n, m = matrix.shape
    submatrices = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.sum() == 382:
                        submatrices.append(submatrix)
    return submatrices