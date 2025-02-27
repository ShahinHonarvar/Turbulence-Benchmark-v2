import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if (x - i + 1) * (y - j + 1) == 74:
                        if np.sum(mat[i:x + 1, j:y + 1]) == 74:
                            count += 1
    return count