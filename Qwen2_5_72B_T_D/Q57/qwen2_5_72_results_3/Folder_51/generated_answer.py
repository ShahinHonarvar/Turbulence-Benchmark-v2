import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(matrix, row, col, rows, cols):
        submatrices = []
        for start_row in range(row, rows):
            for end_row in range(start_row, rows):
                for start_col in range(col, cols):
                    for end_col in range(start_col, cols):
                        submatrix = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(submatrix)
        return submatrices
    rows, cols = matrix.shape
    all_submatrices = generate_submatrices(matrix, 0, 0, rows, cols)
    result = [submatrix for submatrix in all_submatrices if np.sum(submatrix) == -46]
    return result