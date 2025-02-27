import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(mat):
        submatrices = []
        for start_row in range(mat.shape[0]):
            for start_col in range(mat.shape[1]):
                for end_row in range(start_row + 1, mat.shape[0] + 1):
                    for end_col in range(start_col + 1, mat.shape[1] + 1):
                        submatrices.append(mat[start_row:end_row, start_col:end_col])
        return submatrices
    all_submatrices = get_submatrices(matrix)
    result = [submat for submat in all_submatrices if np.sum(submat) == 13]
    return result