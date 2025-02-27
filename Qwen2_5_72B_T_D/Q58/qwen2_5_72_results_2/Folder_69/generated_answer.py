import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    count = 0
    target_size = 126
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i + 1, matrix.shape[0] + 1):
                for y in range(j + 1, matrix.shape[1] + 1):
                    if (x - i) * (y - j) == target_size:
                        count += 1
    return count