import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for h in range(1, rows + 1):
        for w in range(1, cols + 1):
            for i in range(rows - h + 1):
                for j in range(cols - w + 1):
                    submatrix = matrix[i:i + h, j:j + w]
                    if submatrix.size == 127:
                        count += 1
    return count