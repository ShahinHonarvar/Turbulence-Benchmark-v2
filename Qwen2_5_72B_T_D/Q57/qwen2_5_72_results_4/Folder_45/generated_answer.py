import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_all_submatrices(mat):
        submatrices = []
        rows, cols = mat.shape
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submatrices.append(mat[start_row:end_row + 1, start_col:end_col + 1])
        return submatrices
    target_sum = -77
    matching_submatrices = []
    submatrices = get_all_submatrices(np.array(matrix))
    for sub in submatrices:
        if sub.sum() == target_sum:
            matching_submatrices.append(sub)
    return matching_submatrices