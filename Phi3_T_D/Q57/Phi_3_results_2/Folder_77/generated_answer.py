import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    matrix_sum = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            if i > 0:
                matrix_sum[i][j] += matrix_sum[i - 1][j]
            if j > 0:
                matrix_sum[i][j] += matrix_sum[i][j - 1]
            if i > 0 and j > 0:
                matrix_sum[i][j] -= matrix_sum[i - 1][j - 1]
            matrix_sum[i][j] += matrix[i][j]
    for top in range(rows):
        for down in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    window_sum = matrix_sum[down][right]
                    if top > 0:
                        window_sum -= matrix_sum[top - 1][right]
                    if left > 0:
                        window_sum -= matrix_sum[down][left - 1]
                    if top > 0 and left > 0:
                        window_sum += matrix_sum[top - 1][left - 1]
                    if window_sum == -336:
                        result.append(matrix[top:down + 1, left:right + 1].tolist())
    return result