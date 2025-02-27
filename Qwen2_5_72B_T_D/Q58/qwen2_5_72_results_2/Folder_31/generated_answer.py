import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_n_elements(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for r in range(rows - (n - 1) + 1):
            for c in range(cols - (n - 1) + 1):
                if np.size(matrix[r:r + n, c:c + n]) == n:
                    count += 1
        return count
    return count_submatrices_with_n_elements(matrix, 45)