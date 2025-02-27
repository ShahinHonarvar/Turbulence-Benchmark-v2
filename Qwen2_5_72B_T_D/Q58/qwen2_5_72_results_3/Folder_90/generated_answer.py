import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.prod(matrix[i:i + size, j:j + size].shape) == 176:
                    count += 1
        return count
    if not isinstance(matrix, np.ndarray) or matrix.ndim != 2:
        return 0
    submatrix_size = int(np.sqrt(176))
    if submatrix_size * submatrix_size != 176:
        return 0
    return count_submatrices_of_size(matrix, submatrix_size)