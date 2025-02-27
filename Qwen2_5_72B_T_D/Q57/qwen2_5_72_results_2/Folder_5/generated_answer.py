import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for row_start in range(rows):
            for row_end in range(row_start + 1, rows + 1):
                for col_start in range(cols):
                    for col_end in range(col_start + 1, cols + 1):
                        yield mat[row_start:row_end, col_start:col_end]
    result = [submat.tolist() for submat in get_submatrices(matrix) if np.sum(submat) == -43]
    return result