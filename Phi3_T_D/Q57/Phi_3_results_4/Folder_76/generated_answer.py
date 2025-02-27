import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a two-dimensional numpy matrix')
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start, rows):
            sub_matrix = matrix[row_start:row_end + 1]
            if sub_matrix.size > 0:
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        if col_end == col_start:
                            submat = sub_matrix[sub_matrix[:, col_start] != 0, :]
                        else:
                            submat = sub_matrix[:, col_start:col_end + 1]
                        if submat.sum() == -255:
                            submat_shape = submat.shape
                            row_slice = slice(row_start, row_end + 1)
                            col_slice = slice(col_start, col_end + 1)
                            sub_slice = (row_slice, col_slice)
                            result.append((submat_shape, sub_slice))
    return result