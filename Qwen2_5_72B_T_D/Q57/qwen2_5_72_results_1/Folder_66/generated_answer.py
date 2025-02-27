import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for row_start in range(rows):
            for row_end in range(row_start + 1, rows + 1):
                for col_start in range(cols):
                    for col_end in range(col_start + 1, cols + 1):
                        sub = mat[row_start:row_end, col_start:col_end]
                        submatrices.append(sub)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [sub for sub in submatrices if np.sum(sub) == 99]
    return result