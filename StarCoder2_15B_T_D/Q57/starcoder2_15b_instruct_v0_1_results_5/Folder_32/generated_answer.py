import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices in `matrix` with a particular sum.
    """
    m, n = matrix.shape
    result = []
    for i in range(m - 2):
        for j in range(n - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.sum() == 901:
                result.append(submatrix)
    return result