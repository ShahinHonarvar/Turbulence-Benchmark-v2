import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 97
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            submat = matrix[i:min(i + 10, rows), j:min(j + 10, cols)]
            if submat.size == target_size:
                count += 1
    return count