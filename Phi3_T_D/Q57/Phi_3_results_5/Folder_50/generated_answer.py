import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(matrix, row_start, row_end, col_start, col_end):
        if row_end == row_start + 1 or col_end == col_start + 1:
            return []
        mid_row, mid_col = ((row_start + row_end) // 2, (col_start + col_end) // 2)
        result = []
        for x, y in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            for subarray in all_submatrices(matrix, row_start, mid_row, col_start, mid_col):
                result.extend([np.concatenate((subarray[0], arr[x][mid_col:]), axis=1) for arr in all_submatrices(matrix, row_start, y, mid_col, col_end)])
            if x == 0:
                result.extend([matrix[row_start:mid_row, mid_col:]])
            else:
                result.extend([np.flip(matrix[y:row_end, col_start:mid_col], axis=0)])
        return result
    return [submatrix for submatrix in all_submatrices(matrix, 0, len(matrix), 0, len(matrix[0])) if submatrix.sum() == 95]