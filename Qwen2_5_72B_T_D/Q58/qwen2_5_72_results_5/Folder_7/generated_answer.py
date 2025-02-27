import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, n):
        count = 0
        matrix_height, matrix_width = matrix.shape
        submatrix_size = int(n ** 0.5)
        for i in range(matrix_height - submatrix_size + 1):
            for j in range(matrix_width - submatrix_size + 1):
                if np.prod(matrix[i:i + submatrix_size, j:j + submatrix_size].shape) == n:
                    count += 1
        return count
    return count_submatrices(matrix, 121)