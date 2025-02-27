import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, target_size):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows - target_size + 1):
            for j in range(cols - target_size + 1):
                if matrix[i:i + target_size, j:j + target_size].size == target_size:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 154)