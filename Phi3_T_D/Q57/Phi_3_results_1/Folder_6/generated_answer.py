import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    total_elements = rows * cols

    def check(pos, shape, total):
        if total < 126:
            return False
        submatrix = matrix[pos[0]:pos[0] + shape[0], pos[1]:pos[1] + shape[1]]
        return np.sum(submatrix) == 126

    def search(ind, rows, cols, left_shape, right_shape, total, path):
        if total == 126:
            result.append([matrix[i[0]:i[0] + left_shape[0], i[1]:i[1] + right_shape[1]] for i in path])
            return
        for r in range(ind, rows):
            for c in range(cols):
                if left_shape[1] <= c <= cols - right_shape[1]:
                    if check((r, c), (left_shape[0], right_shape[1]), total + np.sum(matrix[r, c:c + right_shape[1]])):
                        search(r + 1, rows, cols - c - 1, (left_shape[0], c + 1 - left_shape[1]), right_shape, total + np.sum(matrix[r, c:c + right_shape[1]]), [(r, c), (r, c + right_shape[1])])
    search(0, rows, cols, (1, 1), (rows - 1, cols - 1), 0, [])
    return result