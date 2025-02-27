import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size_row in range(i + 1, rows + 1):
                for size_col in range(j + 1, cols + 1):
                    submatrix = matrix[i:size_row, j:size_col]
                    if np.sum(submatrix) == 69:
                        result.append(submatrix)
    return result