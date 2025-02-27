import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix):
        rows, cols = matrix.shape
        submatrices = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submat = matrix[start_row:end_row + 1, start_col:end_col + 1]
                        submatrices.append(submat)
        return submatrices
    submatrices = all_submatrices(matrix)
    result = [submat for submat in submatrices if np.sum(submat) == -82]
    return result