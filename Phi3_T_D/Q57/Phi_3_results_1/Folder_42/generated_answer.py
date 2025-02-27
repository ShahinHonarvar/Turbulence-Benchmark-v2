import numpy as np

def submatrix_with_particular_sum(matrix):
    n, m = matrix.shape
    res = []

    def find_submatrix(i, j, path, curr_sum):
        if curr_sum == 862:
            submatrix = np.array([matrix[x][path[x]] for x in range(i, j + 1)])
            submatrix_sum = submatrix.sum()
            if submatrix_sum == 862:
                res.append(submatrix)
            return
        if i < n and curr_sum + matrix[i][j] <= 862:
            curr_sum += matrix[i][j]
            find_submatrix(i + 1, j + 1, path, curr_sum)
            curr_sum -= matrix[i][j]
        if j < m and curr_sum + np.sum(matrix[i:, j]) <= 862:
            curr_sum += np.sum(matrix[i:, j])
            find_submatrix(i, j + 1, path, curr_sum)
            curr_sum -= np.sum(matrix[i:, j])
    for i in range(n):
        for j in range(m):
            find_submatrix(i, j, [i, j], 0)
    return res