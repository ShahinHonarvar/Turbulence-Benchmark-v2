import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(m, n, k):
        count = 0
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                submatrix = matrix[i:i + k, j:j + k]
                if np.sum(submatrix.size == 186):
                    count += 1
        return count
    m, n = matrix.shape
    for k in range(1, min(m, n) + 1):
        result = count_submatrices_of_size(m, n, k)
        if result > 0:
            return result
    return 0