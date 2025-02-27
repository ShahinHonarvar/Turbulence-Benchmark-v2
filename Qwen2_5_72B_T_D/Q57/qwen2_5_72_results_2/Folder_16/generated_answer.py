import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submatrix = mat[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(submatrix)
        return submatrices
    submatrices = get_submatrices(matrix)
    result = [submat for submat in submatrices if np.sum(submat) == -157]
    return result