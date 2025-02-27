import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []

    def helper(i, j):
        if i > m or j > n:
            return
        curr_sum = sum((sum(matrix[i:i + k, j:j + l]) for k in range(1, m - i + 1) for l in range(1, n - j + 1)))
        if curr_sum == -81:
            result.append(matrix[i:i + k, j:j + l])
        for x in range(i, m):
            for y in range(j, n):
                helper(x + 1, y + 1)
    helper(0, 0)
    return result