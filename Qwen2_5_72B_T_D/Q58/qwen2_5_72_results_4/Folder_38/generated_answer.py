import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n, target):
        count = 0
        for i in range(m - target + 1):
            for j in range(n - target + 1):
                if np.all(matrix[i:i + target, j:j + target] == 34):
                    count += 1
        return count
    m, n = matrix.shape
    return count_submatrices(m, n, 34)