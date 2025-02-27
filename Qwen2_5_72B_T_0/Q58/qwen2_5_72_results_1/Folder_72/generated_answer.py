import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, rows, cols, size):
        count = 0
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                if np.sum(matrix[i:i + size, j:j + size] == 16) == size * size:
                    count += 1
        return count
    rows, cols = matrix.shape
    return count_submatrices_of_size(matrix, rows, cols, 4)