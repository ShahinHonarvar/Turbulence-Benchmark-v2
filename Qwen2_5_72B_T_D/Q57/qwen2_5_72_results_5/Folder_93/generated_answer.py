import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(mat, rows, cols):
        submatrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        sub = mat[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(sub)
        return submatrices
    submatrices = generate_submatrices(matrix, matrix.shape[0], matrix.shape[1])
    result = [sub for sub in submatrices if np.sum(sub) == -65]
    return result