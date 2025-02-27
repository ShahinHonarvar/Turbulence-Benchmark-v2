import numpy as np

def submatrix_with_n_numbers(matrix):
    mat = np.int64(matrix)
    rows, cols = mat.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for size in range(1, min(rows - i, cols - j) + 1):
                submat = mat[i:i + size, j:j + size]
                if submat.size == 87:
                    count += 1
    return count