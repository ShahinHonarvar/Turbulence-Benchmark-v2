import numpy as np

def submatrix_with_particular_sum(matrix):

    def find_submatrices_with_sum(mat, target_sum, all_submatrices, start_row, start_col):
        for end_row in range(start_row, mat.shape[0]):
            for end_col in range(start_col, mat.shape[1]):
                submat_sum = np.sum(mat[start_row:end_row + 1, start_col:end_col + 1])
                if submat_sum == target_sum:
                    all_submatrices.append(mat[start_row:end_row + 1, start_col:end_col + 1])
    all_submatrices = []
    for start_row in range(matrix.shape[0]):
        for start_col in range(matrix.shape[1]):
            find_submatrices_with_sum(matrix, 88, all_submatrices, start_row, start_col)
    return all_submatrices