import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(matrix, start_row, start_col, rows, cols):
        submatrices = []
        for end_row in range(start_row, rows):
            for end_col in range(start_col, cols):
                submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                submatrices.append(submatrix)
        return submatrices
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for submatrix in generate_submatrices(matrix, i, j, rows, cols):
                if np.sum(submatrix) == -779:
                    result.append(submatrix)
    return result