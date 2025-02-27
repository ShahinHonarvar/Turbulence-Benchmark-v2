import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrix_of_size(matrix, r, c, size):
        count = 0
        for i in range(0, r - size + 1):
            for j in range(0, c - size + 1):
                if np.prod(matrix[i:i + size, j:j + size].flatten().shape) == 78:
                    count += 1
        return count
    r, c = matrix.shape
    size = int(np.ceil(np.sqrt(78)))
    return count_submatrix_of_size(matrix, r, c, size)