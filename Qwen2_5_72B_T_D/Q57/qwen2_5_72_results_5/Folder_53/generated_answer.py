import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        sub_matrices = []
        rows, cols = mat.shape
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        sub_mat = mat[start_row:end_row + 1, start_col:end_col + 1]
                        sub_matrices.append(sub_mat)
        return sub_matrices
    all_submatrices = get_all_submatrices(matrix)
    target_sum_submatrices = [sub for sub in all_submatrices if np.sum(sub) == -37]
    return target_sum_submatrices