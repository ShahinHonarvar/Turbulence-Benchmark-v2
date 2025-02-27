import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        rows, cols = mat.shape
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        yield mat[start_row:end_row, start_col:end_col]
    submatrices = list(get_submatrices(matrix))
    return [submat for submat in submatrices if np.sum(submat) == -157]