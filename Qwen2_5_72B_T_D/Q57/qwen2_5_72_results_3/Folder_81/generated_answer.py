import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrix_sum(row_start, row_end, col_start, col_end):
        return np.sum(matrix[row_start:row_end, col_start:col_end])
    rows, cols = matrix.shape
    result = []
    for row_start in range(rows):
        for row_end in range(row_start + 1, rows + 1):
            for col_start in range(cols):
                for col_end in range(col_start + 1, cols + 1):
                    if submatrix_sum(row_start, row_end, col_start, col_end) == -90:
                        result.append(matrix[row_start:row_end, col_start:col_end])
    return result