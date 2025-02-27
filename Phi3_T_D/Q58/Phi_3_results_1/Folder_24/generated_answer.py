import numpy as np

def submatrix_with_n_numbers(matrix):
    height, width = matrix.shape
    count = 0
    for y in range(height):
        for x in range(width):
            for i in range(y, height):
                for j in range(x, width):
                    submatrix = matrix[y:i + 1, x:j + 1]
                    if submatrix.size == 51:
                        count += 1
    return count