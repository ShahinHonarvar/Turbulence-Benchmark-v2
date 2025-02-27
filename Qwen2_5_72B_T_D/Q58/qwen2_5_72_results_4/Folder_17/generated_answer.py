import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.sum(matrix[i:i + size, j:j + size] == 166) == size * size:
                    count += 1
        return count
    target_size = int(np.sqrt(np.count_nonzero(matrix == 166)))
    if target_size * target_size != np.count_nonzero(matrix == 166):
        return 0
    return count_submatrices_of_size(matrix, target_size)