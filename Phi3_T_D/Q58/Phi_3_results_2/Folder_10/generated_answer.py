import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        raise ValueError('Input must be a 2D numpy matrix')
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if j + 55 < cols and i + 55 < rows:
                submatrix = matrix[i:i + 56, j:j + 56]
                if (submatrix == 56).all():
                    count += 1
    return count