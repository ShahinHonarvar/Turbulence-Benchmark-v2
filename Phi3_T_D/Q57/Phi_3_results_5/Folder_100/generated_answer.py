import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    for i in range(rows):
        for j in range(cols):
            for x_len in range(1, rows - i + 1):
                if x_len > rows - i:
                    break
                for y_len in range(1, cols - j + 1):
                    if y_len > cols - j:
                        break
                    submat = matrix[i:i + x_len, j:j + y_len]
                    if submat.sum() == 28:
                        sub_matrices.append(submat)
    return sub_matrices