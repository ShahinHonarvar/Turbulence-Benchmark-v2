import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size_k(matrix, k):
        count = 0
        rows, cols = matrix.shape
        if k == 147 and rows * cols >= k:
            for i in range(rows - k + 1):
                for j in range(cols - k + 1):
                    if np.prod(matrix[i:i + k, j:j + k].shape) == k:
                        count += 1
        return count
    return count_submatrices_of_size_k(matrix, 147)