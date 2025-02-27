import numpy as np

def submatrix_with_n_numbers(matrix, n=80):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    if (k - i) * (l - j) == n:
                        submatrix = matrix[i:k, j:l]
                        if np.prod(submatrix.shape) == n:
                            count += 1
    return count