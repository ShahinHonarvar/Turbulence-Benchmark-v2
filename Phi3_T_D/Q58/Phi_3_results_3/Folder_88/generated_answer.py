import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for smat in range(1, min(rows, cols) + 1):
        for i in range(rows - smat + 1):
            for j in range(cols - smat + 1):
                submat = matrix[i:i + smat, j:j + smat]
                if submat.size == 67:
                    count += 1
    return count