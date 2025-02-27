import numpy as np

def submatrix_with_n_numbers(matrix):
    target_size = 91
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if (rows - i) * (cols - j) >= target_size:
                submatrix = matrix[i:rows, j:cols]
                if submatrix.size == target_size:
                    count += 1
    return count