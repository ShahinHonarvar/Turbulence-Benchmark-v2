import numpy as np

def submatrix_with_n_numbers(matrix):
    if isinstance(matrix, np.ndarray) and matrix.ndim == 2:
        count = 0
        rows, cols = matrix.shape
        for i in range(rows):
            for j in range(cols):
                for k in range(i, rows):
                    for l in range(j, cols):
                        submarix = matrix[i:k + 1, j:l + 1]
                        if submatrix.size == 13:
                            count += 1
        return count
    return 0