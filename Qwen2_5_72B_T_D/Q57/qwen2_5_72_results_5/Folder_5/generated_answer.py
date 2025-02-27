import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, submatrices_list, start_row, end_row, end_col):
        for rows in range(start_row, end_row + 1):
            for cols in range(end_col + 1):
                sub = matrix[rows:end_row + 1, cols:end_col + 1]
                submatrices_list.append(sub)

    def find_submatrices_with_sum(matrix, target_sum):
        submatrices_list = []
        for start_row in range(matrix.shape[0]):
            for end_row in range(start_row, matrix.shape[0]):
                for end_col in range(matrix.shape[1]):
                    submatrices(matrix, submatrices_list, start_row, end_row, end_col)
        return [sub for sub in submatrices_list if np.sum(sub) == target_sum]
    return find_submatrices_with_sum(matrix, -43)