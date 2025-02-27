import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for height in range(1, rows - i + 1):
                for width in range(1, cols - j + 1):
                    if height * width == 67:
                        submatrix = matrix[i:i + height, j:j + width]
                        if np.size(submatrix) == 67:
                            count += 1
    return count