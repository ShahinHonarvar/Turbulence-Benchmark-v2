import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Find the count of all submatrices of size (n x n) in a given matrix.
    :param matrix: A two-dimensional numpy matrix of integers.
    :return: The count of all submatrices of size (n x n) in the given matrix.
    """
    m, n = matrix.shape
    n = 69
    count = 0
    for i in range(m - n + 1):
        for j in range(n - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            if np.sum(submatrix) == 69:
                count += 1
    return count