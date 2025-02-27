import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = 432
    rows, cols = matrix.shape
    submatrices = []
    n = rows * cols

    def get_submatrix(row_start, col_start, length, height):
        return matrix[row_start:row_start + length, col_start:col_start + height]
    for length in range(1, rows + 1):
        for i in range(rows - length + 1):
            for j in range(cols - length + 1):
                sub_matrix = get_submatrix(i, j, length, length)
                if np.sum(sub_matrix) == target_sum:
                    submatrices.append(sub_matrix.tolist())
    return submatrices