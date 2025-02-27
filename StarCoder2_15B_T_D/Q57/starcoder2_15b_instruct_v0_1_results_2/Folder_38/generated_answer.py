import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list:
    """
    Finds all submatrices of the given matrix such that the sum of all integers in
    each submatrix is 34.
    """
    result = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i + 1, matrix.shape[0] + 1):
                for l in range(j + 1, matrix.shape[1] + 1):
                    submatrix = matrix[i:k, j:l]
                    if sum(submatrix.flatten()) == 34:
                        result.append(submatrix)
    return result