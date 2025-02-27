import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def get_submatrices(r, c, curr_sum):
        if curr_sum == 13:
            result.append(curr_matrix.copy())
            return
        if curr_sum > 13 or r >= rows or c >= cols:
            return
        for i in range(r, rows):
            for j in range(c, cols):
                curr_matrix.append(matrix[i, j])
                get_submatrices(i, j + 1, curr_sum + matrix[i, j])
                curr_matrix.pop()
    for i in range(rows):
        for j in range(cols):
            curr_matrix = []
            get_submatrices(i, j, 0)
    return result