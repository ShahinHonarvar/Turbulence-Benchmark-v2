import numpy as np

def submatrix_with_particular_sum(matrix):

    def get_submatrices(matrix, rows, cols):
        submatrices = []
        for start_row in range(rows):
            for end_row in range(start_row + 1, rows + 1):
                for start_col in range(cols):
                    for end_col in range(start_col + 1, cols + 1):
                        submatrices.append(matrix[start_row:end_row, start_col:end_col])
        return submatrices
    rows, cols = matrix.shape
    submatrices = get_submatrices(matrix, rows, cols)
    result = [submatrix for submatrix in submatrices if np.sum(submatrix) == 752]
    return result