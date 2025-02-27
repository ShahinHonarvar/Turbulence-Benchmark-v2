import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, rows, cols):
        submats = []
        for start_row in range(rows):
            for end_row in range(start_row, rows):
                for start_col in range(cols):
                    for end_col in range(start_col, cols):
                        submats.append(matrix[start_row:end_row + 1, start_col:end_col + 1])
        return submats
    rows, cols = matrix.shape
    all_submatrices = submatrices(matrix, rows, cols)
    target_sum_matrices = [submat for submat in all_submatrices if np.sum(submat) == 40]
    return target_sum_matrices