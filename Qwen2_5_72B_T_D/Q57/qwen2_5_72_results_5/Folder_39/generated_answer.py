import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        yield mat[row_start:row_end + 1, col_start:col_end + 1]
    result = []
    for submat in get_submatrices(matrix):
        if np.sum(submat) == 66:
            result.append(submat)
    return result