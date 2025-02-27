import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices = []

    def get_cumulative_sum(matrix):
        return np.cumsum(np.cumsum(matrix, axis=0), axis=1)

    def calculate_submatrix_sum(cumulative_matrix, top_left, bottom_right):
        top, left = top_left
        bottom, right = bottom_right
        return cumulative_matrix[bottom, right] - cumulative_matrix[top - 1, right] - cumulative_matrix[bottom, left - 1] + cumulative_matrix[top - 1, left - 1]
    for size in range(1, min(rows, cols) + 1):
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix_sum = calculate_submatrix_sum(get_cumulative_sum(matrix), (i, j), (i + size, j + size))
                if submatrix_sum == -255:
                    submatrices.append(matrix[i:i + size, j:j + size])
    return submatrices