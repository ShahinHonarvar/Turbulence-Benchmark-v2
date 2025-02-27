import numpy as np

def submatrix_with_particular_sum(matrix: np.ndarray) -> list:
    """
    Returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -255.
    """
    return [matrix[i:j, k:l] for i in range(matrix.shape[0]) for j in range(i + 1, matrix.shape[0] + 1) for k in range(matrix.shape[1]) for l in range(k + 1, matrix.shape[1] + 1) if matrix[i:j, k:l].sum() == -255] or []