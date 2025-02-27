import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    def count_submatrices(i, j, n):
        if i + n > rows or j + n > cols:
            return 0
        submatrix = matrix[i:i + n, j:j + n]
        if np.unique(submatrix).size == n:
            return 1
        return 0
    for i in range(rows):
        for j in range(cols):
            for n in range(1, min(rows - i, cols - j) + 1):
                count += count_submatrices(i, j, n)
    return count