import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    num_rows, num_cols = matrix.shape
    num_submatrices = 0
    for row in range(num_rows - 2):
        for col in range(num_cols - 2):
            submatrix = matrix[row:row + 3, col:col + 3]
            num_integers = np.sum(submatrix > 0)
            if num_integers == 9:
                num_submatrices += 1
    return num_submatrices