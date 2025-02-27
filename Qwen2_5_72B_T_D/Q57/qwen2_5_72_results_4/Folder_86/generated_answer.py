import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        sub_matrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        sub_matrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        sub_matrices.append(sub_matrix)
        return sub_matrices
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [sub_matrix for sub_matrix in all_submatrices if np.sum(sub_matrix) == -394]
    return result