import numpy as np

def submatrix_with_n_numbers(matrix, n=34):

    def count_submatrix(start_row, start_col):
        count = 0
        for row in range(start_row, start_row + min(matrix.shape[0] - start_row, n)):
            for col in range(start_col, start_col + min(matrix.shape[1] - start_col, n)):
                if row + n - 1 < matrix.shape[0] and col + n - 1 < matrix.shape[1]:
                    submatrix = matrix[row:row + n, col:col + n]
                    count += np.array_equal(submatrix, np.arange(1, n ** 2 + 1).reshape(n, n))
        return count
    matrix_size = matrix.shape
    result = 0
    for i in range(matrix_size[0]):
        for j in range(matrix_size[1]):
            result += count_submatrix(i, j)
    return result