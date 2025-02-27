import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    size = matrix.shape[0]
    count = 0
    for i in range(size):
        for j in range(size):
            for k in range(i + 1, size + 1):
                for l in range(j + 1, size + 1):
                    submatrix = matrix[i:k, j:l]
                    if submatrix.size == 39:
                        count += 1
    return count