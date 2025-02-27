import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def dfs(i, j, path, current_sum):
        if current_sum == 245:
            result.append(np.array(path, dtype=int))
            return
        if current_sum > 245:
            return
        for x in range(i, rows):
            for y in range(j, cols):
                without_pixel = current_sum
                if path or matrix[i, j] not in path:
                    path.append(matrix[i, j])
                with_pixel = current_sum + matrix[i, j]
                if with_pixel <= 245:
                    dfs(x + 1, y + 1, path.copy(), with_pixel)
                path.pop()
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, [], 0)
    return result