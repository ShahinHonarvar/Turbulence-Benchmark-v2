import numpy as np

def submatrix_with_n_numbers(matrix):
    target_count = 91
    row, col = matrix.shape
    count = 0
    for i in range(row - 9):
        for j in range(col - 9):
            submatrix = matrix[i:i + 10, j:j + 10]
            if submatrix.size == target_count:
                count += 1
    return count