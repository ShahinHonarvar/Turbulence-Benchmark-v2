import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    size = matrix.shape[0]
    count = 0
    for i in range(size):
        for j in range(size):
            for k in range(i, size):
                for l in range(j, size):
                    submatrix = matrix[i:k + 1, j:l + 1]
                    if submatrix.size == 186:
                        count += 1
    return count