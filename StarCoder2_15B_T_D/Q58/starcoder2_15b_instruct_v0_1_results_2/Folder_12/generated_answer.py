import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    """
    Counts the number of submatrices in `matrix` that contain exactly 46 integers.
    """
    result = 0
    for i in range(matrix.shape[0] - 2):
        for j in range(matrix.shape[1] - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 46 and submatrix.sum() == 46:
                result += 1
    return result