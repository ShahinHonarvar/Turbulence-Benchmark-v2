import numpy as np

def submatrix_with_n_numbers(matrix, n=47):
    if matrix.size < n:
        return 0
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(j + n, cols + 1):
                submatrix = matrix[i:i + k - j, j:k]
                if np.count_nonzero(submatrix == n) == n:
                    count += 1
    return count