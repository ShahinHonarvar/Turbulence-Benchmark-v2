import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(k):
        count = 0
        for i in range(matrix.shape[0] - k + 1):
            for j in range(matrix.shape[1] - k + 1):
                if np.size(matrix[i:i + k, j:j + k]) == 115:
                    count += 1
        return count
    for size in range(1, min(matrix.shape) + 1):
        if size * size == 115:
            return count_submatrices_of_size(size)
    return 0