import numpy as np

def submatrix_with_particular_sum(matrix):
    max_size = min(matrix.shape)
    result = []

    def check_submatrix(start_row, start_col):
        temp_matrix = matrix[start_row:max_size, start_col:max_size]
        return np.sum(temp_matrix) == 99
    for size in range(1, max_size + 1):
        for row in range(matrix.shape[0] - size + 1):
            for col in range(matrix.shape[1] - size + 1):
                if check_submatrix(row, col, size):
                    result.append(matrix[row:row + size, col:col + size].tolist())
    return result