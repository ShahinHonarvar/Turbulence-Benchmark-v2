import numpy as np
from itertools import product

def submatrix_with_particular_sum(matrix):

    def check_submatrix(matrix, upper_left, lower_right, target_sum):
        return np.sum(matrix[upper_left[0]:lower_right[0] + 1, upper_left[1]:lower_right[1] + 1]) == target_sum
    matrix = np.array(matrix)
    rows, cols = matrix.shape
    matched_submatrices = []
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if check_submatrix(matrix, (i, j), (k, l), -255):
                        matched_submatrices.append(matrix[i:k + 1, j:l + 1].tolist())
    return matched_submatrices