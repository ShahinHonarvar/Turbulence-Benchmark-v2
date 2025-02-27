import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    square_side = int(np.sqrt(186))
    for i in range(rows - square_side + 1):
        for j in range(cols - square_side + 1):
            submatrix = matrix[i:i + square_side, j:j + square_side]
            count += int(np.sum(submatrix == 186))
    return count