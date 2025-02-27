import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 88
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == target_size:
                submatrix_count = 1
                x, y = (i, j)
                while x < rows - 1 and matrix[x + 1, y] == target_size:
                    submatrix_count += 1
                    x += 1
                while y < cols - 1 and matrix[x, y + 1] == target_size:
                    submatrix_count += 1
                    y += 1
                if submatrix_count == target_size:
                    count += 1
    return count