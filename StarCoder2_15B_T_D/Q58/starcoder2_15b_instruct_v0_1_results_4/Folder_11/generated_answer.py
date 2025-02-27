import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices in a given matrix that contain 38 integers each.

    Args:
        matrix (np.ndarray): A two-dimensional numpy matrix of integers.

    Returns:
        int: The number of submatrices that contain 38 integers each.
    """
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 38:
                        count += 1
    return count