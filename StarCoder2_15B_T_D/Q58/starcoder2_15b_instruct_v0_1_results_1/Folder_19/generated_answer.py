import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 16):
        for j in range(len(matrix[0]) - 16):
            submatrix = matrix[i:i + 17, j:j + 17]
            if submatrix.size == 17:
                count += 1
    return count