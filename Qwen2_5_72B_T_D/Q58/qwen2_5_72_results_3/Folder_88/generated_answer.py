import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(n, matrix):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if np.prod(matrix[i:i + n, j:j + n].shape) == 67:
                    count += 1
        return count
    return count_submatrices_of_size(1, matrix) if 67 in matrix else count_submatrices_of_size(int(np.sqrt(67)), matrix)