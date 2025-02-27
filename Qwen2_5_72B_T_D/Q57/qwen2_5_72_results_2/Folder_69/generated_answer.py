import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat, r, c):
        for rows in range(1, r + 1):
            for cols in range(1, c + 1):
                for start_row in range(0, r - rows + 1):
                    for start_col in range(0, c - cols + 1):
                        yield mat[start_row:start_row + rows, start_col:start_col + cols]
    result = []
    rows, cols = matrix.shape
    for submatrix in get_submatrices(matrix, rows, cols):
        if np.sum(submatrix) == 752:
            result.append(submatrix)
    return result