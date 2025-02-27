import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        if n == 1:
            return np.sum(matrix == n)
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if np.sum(matrix[i:i + n, j:j + n]) == n * n * 1:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 51)