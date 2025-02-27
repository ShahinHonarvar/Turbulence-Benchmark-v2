import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(k):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - k + 1):
            for j in range(cols - k + 1):
                if np.sum(matrix[i:i + k, j:j + k].size == 59):
                    count += 1
        return count
    return count_submatrices_of_size(1) + count_submatrices_of_size(2) + count_submatrices_of_size(3) + count_submatrices_of_size(4)