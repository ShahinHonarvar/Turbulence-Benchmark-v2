import numpy as np

def submatrix_with_particular_sum(matrix):

    def all_submatrices(m, n):
        for top_row in range(m):
            for bot_row in range(top_row, m):
                for left_col in range(n):
                    for right_col in range(left_col, n):
                        yield m[top_row:bot_row + 1, left_col:right_col + 1]
    rows, cols = matrix.shape
    found_submatrices = []
    for submatrix in all_submatrices(rows, cols):
        if submatrix.sum() == 54:
            found_submatrices.append(submatrix.tolist())
    return found_submatrices