import numpy as np

def submatrix_with_n_numbers(matrix):

    def count_submatrices_with_sum(matrix, target_sum):
        rows, cols = matrix.shape
        count = 0
        for i in range(rows):
            for j in range(cols):
                current_sum = 0
                for k in range(i, rows):
                    for l in range(j, cols):
                        current_sum += matrix[k, l]
                        if current_sum == target_sum:
                            count += 1
        return count
    return count_submatrices_with_sum(matrix, 103)