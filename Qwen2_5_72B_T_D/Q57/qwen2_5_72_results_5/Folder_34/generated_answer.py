import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submatrices_list = []
        for start_row in range(rows):
            for end_row in range(start_row + 1, rows + 1):
                for start_col in range(cols):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrices_list.append(matrix[start_row:end_row, start_col:end_col])
        return submatrices_list
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == -13]
    return result