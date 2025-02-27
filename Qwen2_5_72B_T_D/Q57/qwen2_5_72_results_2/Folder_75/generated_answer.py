import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        r, c = mat.shape
        for width in range(1, c + 1):
            for height in range(1, r + 1):
                for start_row in range(r - height + 1):
                    for start_col in range(c - width + 1):
                        yield mat[start_row:start_row + height, start_col:start_col + width]
    sub_matrices = [submat for submat in get_submatrices(matrix) if np.sum(submat) == 16]
    return sub_matrices