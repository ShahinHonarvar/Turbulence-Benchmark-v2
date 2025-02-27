import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []

    def dfs(upper, lower, left, right, target, current_sum):
        if current_sum == target:
            result.append(matrix[upper:lower + 1, left:right + 1].tolist())
            return
        if current_sum > target or upper >= rows or left >= cols:
            return
        dfs(upper + 1, lower, left, right, target, current_sum + matrix[upper + 1][left])
        dfs(upper, lower, left + 1, right, target, current_sum + matrix[upper][left + 1])
        dfs(upper + 1, lower, left + 1, right, target, current_sum + matrix[upper + 1][left + 1])
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    dfs(i, k, j, l, -81, matrix[i][j])
    return result