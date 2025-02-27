import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_submatrix_sum(row_start, col_start):
        return np.sum(matrix[row_start:row_start + sub_rows, col_start:col_start + sub_cols])
    for i in range(rows):
        for j in range(cols):
            for sub_rows in range(1, rows - i + 1):
                for sub_cols in range(1, cols - j + 1):
                    if get_submatrix_sum(i, j) == -47:
                        result.append(matrix[i:i + sub_rows, j:j + sub_cols])
    return result