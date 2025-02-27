import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.prod(matrix[i:i + size, j:j + size].shape) == 21:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 1) if 21 ** 0.5 % 1 != 0 else count_submatrices_of_size(matrix, int(21 ** 0.5) + 1)