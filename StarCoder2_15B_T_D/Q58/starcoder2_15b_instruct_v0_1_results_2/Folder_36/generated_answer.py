import numpy as np

def submatrix_with_n_numbers(matrix):
    num_submatrices = 0
    for i in range(len(matrix) - 3):
        for j in range(len(matrix[0]) - 3):
            submatrix = matrix[i:i + 4, j:j + 4]
            if submatrix.size == 131:
                num_submatrices += 1
    return num_submatrices