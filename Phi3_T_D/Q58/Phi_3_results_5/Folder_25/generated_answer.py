import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    if height == 0 or width == 0:
        return 0
    count = 0
    n = 66
    for i in range(height):
        for j in range(width):
            vertical = 0
            horizontal = 0
            diagonal = 0
            off_diagonal = 0
            crossing = 0
            for k in range(n):
                if i + k < height and j + k < width:
                    diagonal = 1 + (matrix[i + k, j + k] == matrix[i, j])
                    off_diagonal = 1 + (matrix[i + k, width - j - 1] == matrix[i, j])
                elif i + k < height and j - k >= 0:
                    vertical = 1 + (matrix[i + k, j] == matrix[i, j])
                    crossing = 1 + (matrix[i + k, j - k] == matrix[i, j])
                else:
                    break
                if vertical >= n and horizontal >= n and (diagonal >= n) and (off_diagonal >= n) and (crossing >= n):
                    count += 1
                horizontal += 1
            vertical = 0
            horizontal = 0
            diagonal = 0
            off_diagonal = 0
            crossing = 0
            for k in range(n):
                if i - k >= 0 and j + k < width:
                    diagonal = 1 + (matrix[i - k, j + k] == matrix[i, j])
                    off_diagonal = 1 + (matrix[height - i - 1, j - k] == matrix[i, j])
                elif i >= 0 and j + k < width:
                    vertical = 1 + (matrix[i, j + k] == matrix[i, j])
                    crossing = 1 + (matrix[i - k, j - k] == matrix[i, j])
                else:
                    break
                if vertical >= n and horizontal >= n and (diagonal >= n) and (off_diagonal >= n) and (crossing >= n):
                    count += 1
                horizontal += 1
    return count