import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    n = 186
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            if j + n <= cols and i + n <= rows:
                submatrix = matrix[i:i + n, j:j + n]
                if np.count_nonzero(submatrix) == n * n:
                    count += 1
    return count