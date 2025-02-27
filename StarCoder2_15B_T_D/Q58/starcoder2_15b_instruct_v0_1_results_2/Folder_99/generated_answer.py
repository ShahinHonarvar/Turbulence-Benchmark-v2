import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    :param matrix: Two-dimensional numpy matrix of integers
    :return: Count of all submatrices of the given matrix that contain 146 integers each
    """
    num_submatrices = 0
    n = 146
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == n:
                        num_submatrices += 1
    return num_submatrices