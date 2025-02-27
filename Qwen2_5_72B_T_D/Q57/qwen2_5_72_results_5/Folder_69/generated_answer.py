import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(mat):
        row_count, col_count = mat.shape
        for rows in range(1, row_count + 1):
            for cols in range(1, col_count + 1):
                for start_row in range(row_count - rows + 1):
                    for start_col in range(col_count - cols + 1):
                        yield mat[start_row:start_row + rows, start_col:start_col + cols]
    result = [submat.tolist() for submat in all_submatrices(matrix) if np.sum(submat) == 752]
    return result