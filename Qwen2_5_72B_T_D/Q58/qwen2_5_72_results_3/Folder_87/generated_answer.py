import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_of_size(matrix, n):
        count = 0
        rows, cols = matrix.shape
        for i in range(rows - n + 1):
            for j in range(cols - n + 1):
                if matrix[i:i + n, j:j + n].size == 96:
                    count += 1
        return count
    return count_submatrices_of_size(matrix, 96)