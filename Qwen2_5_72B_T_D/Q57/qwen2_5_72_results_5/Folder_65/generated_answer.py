import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        row_count, col_count = mat.shape
        submatrices = []
        for start_row in range(row_count):
            for end_row in range(start_row, row_count):
                for start_col in range(col_count):
                    for end_col in range(start_col, col_count):
                        submatrices.append(mat[start_row:end_row + 1, start_col:end_col + 1])
        return submatrices
    all_submatrices = get_all_submatrices(matrix)
    result = [submat for submat in all_submatrices if np.sum(submat) == 78]
    return result