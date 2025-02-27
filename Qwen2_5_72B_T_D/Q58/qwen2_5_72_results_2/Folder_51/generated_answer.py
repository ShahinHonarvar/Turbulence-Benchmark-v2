import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices(row, col, n):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if 0 <= i < matrix.shape[0] and 0 <= j < matrix.shape[1]:
                    if matrix[i, j] == n:
                        count += 1
        return count
    target_count = 95
    result = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if count_submatrices(i, j, matrix[i, j]) == target_count:
                result += 1
    return result