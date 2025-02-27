import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_sum(matrix, target_sum):
        if not matrix.size:
            return 0
        rows, cols = matrix.shape
        prefix_sum = np.zeros((rows + 1, cols + 1), dtype=int)
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix_sum[i][j] = matrix[i - 1][j - 1] + prefix_sum[i - 1][j] + prefix_sum[i][j - 1] - prefix_sum[i - 1][j - 1]
        count = 0
        for r1 in range(rows):
            for c1 in range(cols):
                for r2 in range(r1, rows):
                    for c2 in range(c1, cols):
                        submatrix_sum = prefix_sum[r2 + 1][c2 + 1] - prefix_sum[r1][c2 + 1] - prefix_sum[r2 + 1][c1] + prefix_sum[r1][c1]
                        if submatrix_sum == target_sum:
                            count += 1
        return count
    return count_submatrices_with_sum(matrix, 69)