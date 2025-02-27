import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    """
    Finds the count of all submatrices in `matrix` that contain 73 integers each.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.size == 73:
                count += 1
    return count