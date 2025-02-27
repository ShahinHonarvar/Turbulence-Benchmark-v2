import numpy as np

def submatrix_with_particular_sum(matrix):

    def check_sum(sub_matrix):
        return np.sum(sub_matrix) == -26
    submatrices = []
    height, width = matrix.shape
    for start_row in range(height):
        for start_col in range(width):
            for end_row in range(start_row, height):
                for end_col in range(start_col, width):
                    submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                    if check_sum(submatrix):
                        submatrices.append(submatrix)
    return submatrices