import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.prod(matrix[i:i + size, j:j + size].flatten() == 27) == 1:
                    count += 1
        return count
    size = int(np.sqrt(27))
    if size * size != 27:
        return 0
    return count_submatrices_of_size(matrix, size)