import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    height, width = matrix.shape
    size = height * width
    count_78 = 0
    for i in range(height):
        for j in range(width):
            for k in range(height - i):
                for l in range(width - j):
                    submatrix = matrix[i:i + k, j:j + l]
                    if np.all(submatrix == 78) and submatrix.size == 78:
                        count_78 += 1
    return count_78