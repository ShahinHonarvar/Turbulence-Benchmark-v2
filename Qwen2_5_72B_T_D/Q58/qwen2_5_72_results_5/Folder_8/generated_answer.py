import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(n):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if np.prod(matrix[i:i + n, j:j + n].shape) == 29:
                    count += 1
        return count
    return count_submatrices_of_size(1) + count_submatrices_of_size(2) + count_submatrices_of_size(3) + count_submatrices_of_size(4) + count_submatrices_of_size(5)