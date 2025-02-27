import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    result = []

    def search_submatrix(x, y, current_submatrix, total_sum):
        if total_sum == 411:
            result.append(current_submatrix[:])
            return
        for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            next_x, next_y = (x + dx, y + dy)
            if 0 <= next_x < m and 0 <= next_y < n:
                next_submatrix = current_submatrix + [(next_x, next_y)]
                next_sum = total_sum + matrix[next_x, next_y]
                search_submatrix(next_x, next_y, next_submatrix, next_sum)
    for i in range(m):
        for j in range(n):
            search_submatrix(i, j, [(i, j)], matrix[i, j])
    return result