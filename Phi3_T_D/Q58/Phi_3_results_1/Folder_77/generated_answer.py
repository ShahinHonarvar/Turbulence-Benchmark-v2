import numpy as np

def submatrix_with_n_numbers(matrix, n=179):
    if matrix.shape[0] < n or matrix.shape[1] < n:
        return 0
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - n + 1):
        for j in range(cols - n + 1):
            submatrix = matrix[i:i + n, j:j + n]
            count += np.all(submatrix == 179)
    return count