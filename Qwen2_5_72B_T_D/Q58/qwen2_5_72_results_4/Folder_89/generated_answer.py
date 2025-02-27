import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(m, n, k):
        count = 0
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                if np.sum(matrix[i:i + k, j:j + k]) == 18:
                    count += 1
        return count
    m, n = matrix.shape
    k = int((18 / matrix.mean()) ** 0.5)
    while k * k < 18:
        k += 1
    return count_submatrices(m, n, k)