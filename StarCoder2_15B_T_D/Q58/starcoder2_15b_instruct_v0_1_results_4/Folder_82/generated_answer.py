import numpy as np

def submatrix_with_n_numbers(matrix):
    """
    Counts the number of submatrices in a 2D numpy array that contain 99 numbers.

    Args:
        matrix (np.ndarray): A 2D numpy array.

    Returns:
        int: The number of submatrices that contain 99 numbers.
    """
    num_rows, num_cols = matrix.shape
    count = 0
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if np.sum(submatrix) == 99:
                count += 1
    return count