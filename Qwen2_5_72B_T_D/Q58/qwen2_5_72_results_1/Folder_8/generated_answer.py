import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(k):
        count = 0
        for i in range(matrix.shape[0] - k + 1):
            for j in range(matrix.shape[1] - k + 1):
                if np.size(matrix[i:i + k, j:j + k], axis=None) == 29:
                    count += 1
        return count
    return count_submatrices_of_size(1) if matrix.size < 29 else count_submatrices_of_size(5)