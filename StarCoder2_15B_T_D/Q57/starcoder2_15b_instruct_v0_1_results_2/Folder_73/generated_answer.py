import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Find submatrices of a given matrix with a particular sum.

    Args:
        matrix (np.ndarray): A two-dimensional numpy matrix of integers.

    Returns:
        list: A list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 93. If no such submatrix is found, an empty list is returned.
    """
    submatrices = []
    n_rows, n_cols = matrix.shape
    for row_start in range(n_rows):
        for col_start in range(n_cols):
            for row_end in range(row_start + 1, n_rows + 1):
                for col_end in range(col_start + 1, n_cols + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == 93:
                        submatrices.append(submatrix)
    return submatrices