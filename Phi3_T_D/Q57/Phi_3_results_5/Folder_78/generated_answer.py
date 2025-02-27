import numpy as np

def submatrix_with_particular_sum(matrix):

    def helper(i, j, size, current_sum, current_matrix):
        if size == 0:
            if current_sum == 17:
                result.append(np.copy(current_matrix))
            return
        for step in range(1, size + 1):
            current_matrix[step - 1] = matrix[i:i + step]
            current_sum += matrix[i][j]
            helper(i + step - 1, j, size - 1, current_sum, current_matrix)
            current_sum -= matrix[i][j]
    n_rows = matrix.shape[0]
    n_cols = matrix.shape[1]
    result = []
    for size in range(1, min(n_rows, n_cols) + 1):
        for i in range(n_rows - size + 1):
            for j in range(n_cols - size + 1):
                helper(i, j, size, 0, np.empty((size, size), dtype=int))
    return result