import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices of the given matrix such that the sum of all integers in each submatrix equals -26.
    """
    submatrices = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for m in range(i, len(matrix)):
                for n in range(j, len(matrix[0])):
                    submatrix = matrix[i:m + 1, j:n + 1]
                    if submatrix.sum() == -26:
                        submatrices.append(submatrix)
    return submatrices