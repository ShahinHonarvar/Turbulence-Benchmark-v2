import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, start_row, start_col, rows, cols):
        submatrices_list = []
        for row_end in range(start_row + 1, rows + 1):
            for col_end in range(start_col + 1, cols + 1):
                sub = matrix[start_row:row_end, start_col:col_end]
                submatrices_list.append(sub)
        return submatrices_list
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for sub in submatrices(matrix, i, j, rows, cols):
                if np.sum(sub) == -185:
                    result.append(sub)
    return result