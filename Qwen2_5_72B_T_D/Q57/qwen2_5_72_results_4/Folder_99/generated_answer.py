import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        rows, cols = mat.shape
        submatrices = []
        for start_row in range(rows):
            for start_col in range(cols):
                for end_row in range(start_row + 1, rows + 1):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrices.append(mat[start_row:end_row, start_col:end_col])
        return submatrices
    target_sum = -185
    valid_submatrices = []
    all_submatrices = get_all_submatrices(matrix)
    for submat in all_submatrices:
        if np.sum(submat) == target_sum:
            valid_submatrices.append(submat)
    return valid_submatrices