import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(1, rows - i + 1):
                for sub_size in range(1, cols - j + 1):
                    submat = matrix[i:i + size, j:j + sub_size]
                    if np.count_nonzero(submat == 159) == sub_size * size:
                        count += 1
    return count