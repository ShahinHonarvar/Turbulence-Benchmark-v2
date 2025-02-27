import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for height in range(1, rows + 1):
        for width in range(1, cols + 1):
            for i in range(rows - height + 1):
                for j in range(cols - width + 1):
                    if np.sum(matrix[i:i + height, j:j + width]) == 104:
                        count += 1
    return count