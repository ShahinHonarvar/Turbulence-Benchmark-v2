import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def sum_submatrix(top_left, bottom_right):
        (tl_row, tl_col), (br_row, br_col) = (top_left, bottom_right)
        return matrix[tl_row:br_row + 1, tl_col:br_col + 1].sum()
    for tl_row in range(rows):
        for tl_col in range(cols):
            for br_row in range(tl_row, rows):
                for br_col in range(tl_col, cols):
                    if sum_submatrix((tl_row, tl_col), (br_row, br_col)) == -779:
                        submatrices.append(matrix[tl_row:br_row + 1, tl_col:br_col + 1])
    return submatrices