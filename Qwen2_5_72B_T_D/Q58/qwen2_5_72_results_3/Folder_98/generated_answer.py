import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        rows, cols = matrix.shape
        submatrix_size = int(np.sqrt(n))
        for i in range(rows - submatrix_size + 1):
            for j in range(cols - submatrix_size + 1):
                if np.unique(matrix[i:i + submatrix_size, j:j + submatrix_size].flatten()).size == n:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 9)