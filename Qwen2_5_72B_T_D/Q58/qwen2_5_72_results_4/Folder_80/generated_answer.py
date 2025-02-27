import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        submatrix_count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if np.size(matrix[i:i + n, j:j + n]) == 180:
                    submatrix_count += 1
        return submatrix_count
    return count_submatrices(matrix, 15)