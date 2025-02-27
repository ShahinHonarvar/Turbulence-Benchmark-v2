import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2 or matrix.dtype != int:
        raise ValueError('Input must be a two-dimensional numpy matrix of integers.')

    def all_submatrices(matrix):
        submatrices_list = []
        rows, cols = matrix.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        submatrix = matrix[row_start:row_end + 1, col_start:col_end + 1]
                        submatrices_list.append(submatrix)
        return submatrices_list
    target_sum = 8
    required_submatrices = []
    for submatrix in all_submatrices(matrix):
        if submatrix.sum() == target_sum:
            required_submatrices.append(submatrix)
    return required_submatrices