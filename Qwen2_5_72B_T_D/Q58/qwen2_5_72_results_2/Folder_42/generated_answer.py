import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    target_size = 193
    rows, cols = matrix.shape
    submatrix_area = rows * cols // target_size
    if submatrix_area * target_size != rows * cols:
        return 0
    for i in range(0, rows - rows // submatrix_area + 1):
        for j in range(0, cols - cols // submatrix_area + 1):
            submatrix = matrix[i:i + rows // submatrix_area, j:j + cols // submatrix_area]
            if submatrix.size == target_size:
                count += 1
    return count