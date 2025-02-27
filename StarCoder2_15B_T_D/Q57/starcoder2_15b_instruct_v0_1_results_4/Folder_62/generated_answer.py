import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    This function takes a 2D numpy matrix of integers as input and returns a list of all
    submatrices of the given matrix such that the sum of all integers in each submatrix
    equals 394. If no such submatrix is found, an empty list is returned.
    """
    result = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(submatrix) == 394:
                        result.append(submatrix)
    return result