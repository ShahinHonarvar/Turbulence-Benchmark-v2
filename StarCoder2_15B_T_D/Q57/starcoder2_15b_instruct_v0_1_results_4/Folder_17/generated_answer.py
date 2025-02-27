import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Finds all submatrices in a given 2D numpy matrix whose sum is 398.

    Args:
        matrix (np.ndarray): A 2D numpy matrix of integers.

    Returns:
        list: A list of all submatrices whose sum is 398. Each submatrix is represented as a tuple of (row_start, row_end, col_start, col_end), where row_start and col_start are the starting indices of the submatrix in the original matrix.
    """
    m, n = matrix.shape
    submatrices = []
    for row_start in range(m):
        for row_end in range(row_start + 1, m + 1):
            for col_start in range(n):
                for col_end in range(col_start + 1, n + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == 398:
                        submatrices.append((row_start, row_end, col_start, col_end))
    return submatrices