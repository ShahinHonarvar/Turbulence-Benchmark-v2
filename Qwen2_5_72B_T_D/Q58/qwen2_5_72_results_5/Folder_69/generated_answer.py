import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(m, n, size):
        count = 0
        for i in range(m - size + 1):
            for j in range(n - size + 1):
                if np.sum(matrix[i:i + size, j:j + size]) == 126 * size:
                    count += 1
        return count
    m, n = matrix.shape
    size = int(np.sqrt(matrix.size // 126))
    if size * size * 126 != matrix.size:
        return 0
    return count_submatrices_of_size(m, n, size)