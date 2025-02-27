import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        count = 0
        for i in range(matrix.shape[0] - size + 1):
            for j in range(matrix.shape[1] - size + 1):
                if matrix[i:i + size, j:j + size].size == 138:
                    count += 1
        return count
    size = int(np.sqrt(138))
    if size * size != 138:
        return 0
    return count_submatrices_of_size(matrix, size)