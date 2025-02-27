import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns a list of submatrices of the given matrix such that the sum of all integers in each submatrix equals 616.
    """
    submatrices = []
    n, m = matrix.shape
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if np.sum(sub_matrix) == 616:
                        submatrices.append(sub_matrix)
    return submatrices