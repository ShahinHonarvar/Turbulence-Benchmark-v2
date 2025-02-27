import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size_kxk(mat, k, n):
        count = 0
        rows, cols = mat.shape
        if k * k != n or k > rows or k > cols:
            return 0
        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                if np.sum(mat[i:i + k, j:j + k]) == n:
                    count += 1
        return count
    return count_submatrices_of_size_kxk(matrix, 5, 15)