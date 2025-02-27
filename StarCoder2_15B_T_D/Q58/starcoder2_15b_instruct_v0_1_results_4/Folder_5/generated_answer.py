import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    """
    Returns the count of all submatrices of the given matrix that contain 63 integers each.
    """
    if matrix.size < 63:
        return 0
    num_submatrices = 0
    for i in range(matrix.shape[0] - 8 + 1):
        for j in range(matrix.shape[1] - 8 + 1):
            submatrix = matrix[i:i + 8, j:j + 8]
            if np.sum(submatrix) == 63:
                num_submatrices += 1
    return num_submatrices