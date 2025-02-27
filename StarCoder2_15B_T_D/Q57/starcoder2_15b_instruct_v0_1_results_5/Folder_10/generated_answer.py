import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        raise ValueError('The argument must be a two-dimensional numpy matrix of integers.')
    rows, columns = matrix.shape
    submatrices = []
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(columns):
                for col_end in range(col_start + 1, columns + 1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if submatrix.sum() == 56:
                        submatrices.append(submatrix)
    return submatrices