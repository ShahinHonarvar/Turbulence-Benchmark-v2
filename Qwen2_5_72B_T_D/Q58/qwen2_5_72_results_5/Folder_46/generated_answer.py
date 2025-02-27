import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(matrix, size):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 144:
                    count += 1
        return count
    submatrix_size = int(np.sqrt(144))
    return count_submatrices(matrix, submatrix_size)