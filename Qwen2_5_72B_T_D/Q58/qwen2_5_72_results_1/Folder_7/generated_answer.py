import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_size = 121
    side_length = int(np.sqrt(submatrix_size))
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - side_length + 1):
        for j in range(cols - side_length + 1):
            submatrix = matrix[i:i + side_length, j:j + side_length]
            if submatrix.size == submatrix_size:
                count += 1
    return count