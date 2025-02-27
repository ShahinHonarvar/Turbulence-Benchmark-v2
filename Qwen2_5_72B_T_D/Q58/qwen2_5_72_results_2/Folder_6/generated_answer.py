import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size_kxk(mat, k, target):
        m, n = mat.shape
        count = 0
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                if np.sum(mat[i:i + k, j:j + k] == target) == k * k:
                    count += 1
        return count
    return count_submatrices_of_size_kxk(matrix, 11, 122)