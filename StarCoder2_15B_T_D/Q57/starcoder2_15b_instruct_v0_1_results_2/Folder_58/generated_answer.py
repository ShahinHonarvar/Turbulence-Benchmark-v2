import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -137.
    If no such submatrix is found, the function returns an empty list.
    """
    rows, cols = matrix.shape
    result = []
    for row in range(rows):
        for col in range(cols):
            for row_end in range(row + 1, rows + 1):
                for col_end in range(col + 1, cols + 1):
                    sub_matrix = matrix[row:row_end, col:col_end]
                    if np.sum(sub_matrix) == -137:
                        result.append(sub_matrix)
    return result