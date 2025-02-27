import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = matrix.shape
    result = []
    for rows in range(nrows):
        for cols in range(ncols):
            for target_row in range(nrows - rows):
                for target_col in range(ncols - cols):
                    submatrix_sum = np.sum(matrix[rows:rows + target_row + 1, cols:cols + target_col + 1])
                    if submatrix_sum == -46:
                        result.append(matrix[rows:rows + target_row + 1, cols:cols + target_col + 1])
    return result