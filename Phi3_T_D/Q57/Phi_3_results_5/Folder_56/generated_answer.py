import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def calc_sum(submatrix):
        return np.sum(submatrix)

    def get_submatrix(top_row, left_col, size):
        return matrix[top_row:top_row + size, left_col:left_col + size]
    for size in range(1, min(rows, cols) + 1):
        for r in range(rows - size + 1):
            for c in range(cols - size + 1):
                submatrix = get_submatrix(r, c, size)
                if calc_sum(submatrix) == -50:
                    result.append(submatrix)
    return result