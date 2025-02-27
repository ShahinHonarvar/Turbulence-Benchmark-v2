import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    """
    Finds the count of all submatrices of the given matrix that contain 18 numbers.
    """
    submatrix_count = 0
    rows, cols = matrix.shape
    for i in range(rows - 2):
        for j in range(cols - 2):
            submatrix = matrix[i:i + 3, j:j + 3]
            if submatrix.size == 18 and np.all(np.isin(submatrix, [1, 2, 3, 4, 5, 6, 7, 8, 9])):
                submatrix_count += 1
    return submatrix_count