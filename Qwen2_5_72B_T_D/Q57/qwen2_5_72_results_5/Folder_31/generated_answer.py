import numpy as np

def submatrix_with_particular_sum(matrix):

    def generate_submatrices(matrix, rows, cols):
        submatrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        sub = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(sub)
        return submatrices
    rows, cols = matrix.shape
    all_submatrices = generate_submatrices(matrix, rows, cols)
    result = [sub for sub in all_submatrices if np.sum(sub) == -44]
    return result