import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        sub_matrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        sub_matrices.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
        return sub_matrices
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == -27]
    return result