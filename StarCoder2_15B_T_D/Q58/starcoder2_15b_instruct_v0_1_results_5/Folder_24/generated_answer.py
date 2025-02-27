import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    n_rows, n_cols = matrix.shape
    count = 0
    for i in range(n_rows - 6):
        for j in range(n_cols - 6):
            submatrix = matrix[i:i + 7, j:j + 7]
            if submatrix.size == 51:
                count += 1
    return count