import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for row_start in range(rows):
            for row_end in range(row_start, rows):
                for col_start in range(cols):
                    for col_end in range(col_start, cols):
                        submat = mat[row_start:row_end + 1, col_start:col_end + 1]
                        submatrices.append(submat)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submat for submat in submatrices if np.sum(submat) == 17]
    return result