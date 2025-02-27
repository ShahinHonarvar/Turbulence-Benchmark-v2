import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray) -> int:
    row, col = matrix.shape
    count = 0
    for i in range(row - 1):
        for j in range(col - 1):
            submatrix = matrix[i:i + 2, j:j + 2]
            if submatrix.size == 66:
                count += 1
    return count