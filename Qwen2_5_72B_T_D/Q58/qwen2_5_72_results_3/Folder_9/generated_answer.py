import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                for r in range(1, rows - i + 1):
                    for c in range(1, cols - j + 1):
                        if np.size(matrix[i:i + r, j:j + c]) == n:
                            count += 1
        return count
    return count_submatrices(matrix, 33)