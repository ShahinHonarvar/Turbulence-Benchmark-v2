import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                if sum((1 for _ in np.nditer(matrix[i:i + size, j:j + size]))) == 97:
                    count += 1
    return count