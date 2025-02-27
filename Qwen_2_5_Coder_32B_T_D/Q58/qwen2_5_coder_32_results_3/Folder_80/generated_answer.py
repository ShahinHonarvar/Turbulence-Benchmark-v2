import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    target_size = 180
    count = 0
    for i in range(rows - int(np.sqrt(target_size)) + 1):
        for j in range(cols - int(np.sqrt(target_size)) + 1):
            submatrix = matrix[i:i + int(np.sqrt(target_size)), j:j + int(np.sqrt(target_size))]
            if submatrix.size == target_size:
                count += 1
    return count