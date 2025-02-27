import numpy as np

def submatrix_with_particular_sum(matrix):

    def submatrices(matrix, start_row, start_col, end_row, end_col):
        submatrices_found = []
        for i in range(start_row, end_row + 1):
            for j in range(start_col, end_col + 1):
                sub = matrix[i:end_row + 1, j:end_col + 1]
                submatrices_found.append(sub)
        return submatrices_found
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submat = matrix[i:k + 1, j:l + 1]
                    if np.sum(submat) == -64:
                        result.append(submat)
    return result