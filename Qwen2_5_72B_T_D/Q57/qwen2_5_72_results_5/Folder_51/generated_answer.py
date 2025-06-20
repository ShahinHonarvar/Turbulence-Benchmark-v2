import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        yield mat[row_start:row_end + 1, col_start:col_end + 1]
    target_sum = -46
    submatrices = list(get_submatrices(matrix))
    result = [submat for submat in submatrices if np.sum(submat) == target_sum]
    return result