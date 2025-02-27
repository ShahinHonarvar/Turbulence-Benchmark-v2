import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    total_elements = nrows * ncols
    for left_col in range(ncols):
        for upper_row in range(nrows):
            for right_col in range(left_col, ncols):
                for lower_row in range(upper_row, nrows):
                    submatrix = matrix[upper_row:lower_row + 1, left_col:right_col + 1]
                    if np.sum(submatrix) == -63:
                        result.append(submatrix)
    return result