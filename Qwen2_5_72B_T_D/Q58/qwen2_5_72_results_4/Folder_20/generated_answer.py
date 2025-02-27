import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(m, n, size):
        count = 0
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                if np.prod(np.array([size, size]) == np.unique(matrix[i:i + size, j:j + size], return_counts=True)[1]):
                    count += 1
        return count
    m, n = matrix.shape
    return count_submatrices_of_size(m, n, 7)