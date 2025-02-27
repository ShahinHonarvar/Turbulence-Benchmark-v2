import numpy as np

def submatrix_with_particular_sum(matrix):

    def sum_submatrix(matrix, top_left, bottom_right):
        return np.sum(matrix[top_left[0]:bottom_right[0] + 1, top_left[1]:bottom_right[1] + 1])
    rows, cols = matrix.shape
    result = []
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if sum_submatrix(matrix, (i, j), (x, y)) == -77:
                        result.append(matrix[i:x + 1, j:y + 1].tolist())
    return result