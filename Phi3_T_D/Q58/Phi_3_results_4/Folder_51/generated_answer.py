import numpy as np

def submatrix_with_n_numbers(matrix):
    if len(matrix.shape) != 2 or matrix.dtype != 'int':
        return 0
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for size in range(1, min(rows - i, columns - j) + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if np.prod(submatrix.shape) == size * size and np.all(submatrix == 95):
                    count += 1
    return count