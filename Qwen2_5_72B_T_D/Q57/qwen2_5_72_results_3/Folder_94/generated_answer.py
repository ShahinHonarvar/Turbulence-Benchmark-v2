import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(start_row, start_col, end_row, end_col):
        sub = matrix[start_row:end_row, start_col:end_col]
        return (np.sum(sub), sub)
    rows, cols = matrix.shape
    result = []
    for start_row in range(rows):
        for start_col in range(cols):
            for end_row in range(start_row + 1, rows + 1):
                for end_col in range(start_col + 1, cols + 1):
                    current_sum, sub = submatrix_sum(start_row, start_col, end_row, end_col)
                    if current_sum == 92:
                        result.append(sub.tolist())
    return result