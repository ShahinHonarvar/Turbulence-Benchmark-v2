import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in
    each submatrix equals 28. If no such submatrix is found, returns an empty list.
    """
    submatrices = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for m in range(i, matrix.shape[0]):
                for n in range(j, matrix.shape[1]):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if submatrix.sum() == 28:
                        submatrices.append(submatrix)
    return submatrices