import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    target = 83

    def count_submatrices(r, c, total):
        if total == target:
            return 1
        if total > target:
            return 0
        if r > rows or c > cols:
            return 0
        count = 0
        for i in range(r, rows):
            for j in range(c, cols):
                submatrix_sum = np.sum(matrix[r:i + 1, c:j + 1])
                count += count_submatrices(i + 1, j + 1, submatrix_sum)
        return count
    for i in range(rows):
        for j in range(cols):
            count += count_submatrices(i, j, 0)
    return count