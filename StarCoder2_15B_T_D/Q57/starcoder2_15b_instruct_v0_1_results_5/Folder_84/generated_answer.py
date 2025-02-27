import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns a list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -308.
    If no such submatrix is found, returns an empty list.
    """
    n, m = matrix.shape
    result = []
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    sub_matrix = matrix[i:k + 1, j:l + 1]
                    if sub_matrix.sum() == -308:
                        result.append(sub_matrix)
    return result