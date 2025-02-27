import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Find all submatrices with a sum equal to 1.
    
    :param matrix: 2D numpy matrix of integers.
    :return: List of submatrices with sum equal to 1.
    """
    rows, cols = matrix.shape
    submatrices = []
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    submatrix = matrix[r1:r2 + 1, c1:c2 + 1]
                    if submatrix.sum() == 1:
                        submatrices.append(submatrix)
    return submatrices