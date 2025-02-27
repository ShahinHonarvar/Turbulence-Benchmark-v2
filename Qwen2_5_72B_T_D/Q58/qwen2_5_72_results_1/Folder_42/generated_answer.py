import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_size_k(matrix, k):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                submatrix = matrix[i:i + k, j:j + k]
                if np.count_nonzero(submatrix) == 193:
                    count += 1
        return count
    n = int(np.sqrt(193))
    if n * n != 193:
        return 0
    return count_submatrices_size_k(matrix, n)