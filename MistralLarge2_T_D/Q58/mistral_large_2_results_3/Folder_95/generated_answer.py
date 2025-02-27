import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0

    def count_submatrices(matrix, m, n, num):
        dp = np.zeros((m, n), dtype=int)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == num:
                    dp[i][j] = 0
                else:
                    dp[i][j] = 1 + (dp[i - 1][j] if i > 0 else 0)
        submatrix_count = 0
        for i in range(m):
            for j in range(n):
                min_height = float('inf')
                for k in range(j, -1, -1):
                    min_height = min(min_height, dp[i][k])
                    if min_height * (j - k + 1) == num:
                        submatrix_count += 1
        return submatrix_count
    for num in np.unique(matrix):
        count += count_submatrices(matrix, m, n, num)
    return count