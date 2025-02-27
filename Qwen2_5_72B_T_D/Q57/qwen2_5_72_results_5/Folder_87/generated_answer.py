import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat, r, c):
        sub_matrices = []
        for start_row in range(r):
            for start_col in range(c):
                for end_row in range(start_row + 1, r + 1):
                    for end_col in range(start_col + 1, c + 1):
                        sub_matrices.append(mat[start_row:end_row, start_col:end_col])
        return sub_matrices
    r, c = matrix.shape
    all_submatrices = get_submatrices(matrix, r, c)
    result = [submat for submat in all_submatrices if np.sum(submat) == 35]
    return result