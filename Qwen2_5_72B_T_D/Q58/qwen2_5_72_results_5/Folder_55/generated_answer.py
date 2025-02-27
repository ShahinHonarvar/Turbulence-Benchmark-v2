import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        for i in range(matrix.shape[0] - size + 1):
            for j in range(matrix.shape[1] - size + 1):
                if np.size(matrix[i:i + size, j:j + size]) == 39:
                    count += 1
        return count
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    size = int(np.sqrt(39))
    if size * size != 39:
        return 0
    return count_submatrices_of_size(matrix, size)