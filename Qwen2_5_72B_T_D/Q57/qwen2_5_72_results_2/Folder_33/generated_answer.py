import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, r, c):
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row + 1, r + 1):
                    for end_col in range(start_col + 1, c + 1):
                        yield matrix[start_row:end_row, start_col:end_col]
    r, c = matrix.shape
    result = []
    for submatrix in submatrices(matrix, r, c):
        if np.sum(submatrix) == -811:
            result.append(submatrix.tolist())
    return result