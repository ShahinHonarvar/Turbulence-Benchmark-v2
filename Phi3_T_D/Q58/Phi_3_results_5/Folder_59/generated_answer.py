import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if matrix.ndim != 2 or matrix.size == 0:
        return 0
    matrix_rows, matrix_cols = matrix.shape
    count = 0
    for i in range(matrix_rows):
        for j in range(matrix_cols):
            for size in range(76, matrix_rows + 1):
                if i + size - 1 < matrix_rows and j + 76 <= matrix_cols:
                    count += 1
                else:
                    break
            else:
                continue
            break
    return count