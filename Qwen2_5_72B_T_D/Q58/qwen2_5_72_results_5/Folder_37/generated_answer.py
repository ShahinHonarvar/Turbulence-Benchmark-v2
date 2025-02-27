import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, size):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                submatrix = matrix[i:i + size, j:j + size]
                if submatrix.size == 64:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 8)