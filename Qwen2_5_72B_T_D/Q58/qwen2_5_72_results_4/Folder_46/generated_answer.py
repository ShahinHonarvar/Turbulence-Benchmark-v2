import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(r, c, size):
        count = 0
        for i in range(r - size + 1):
            for j in range(c - size + 1):
                if np.prod(matrix[i:i + size, j:j + size].shape) == 144:
                    count += 1
        return count
    rows, cols = matrix.shape
    if rows * cols < 144:
        return 0
    size = int(np.sqrt(144))
    if size * size != 144 or rows < size or cols < size:
        return 0
    return count_submatrices_of_size(rows, cols, size)