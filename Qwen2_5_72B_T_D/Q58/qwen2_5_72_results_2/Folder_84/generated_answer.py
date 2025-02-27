import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray) or len(matrix.shape) != 2:
        return 0
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 127:
                found = True
                for x in range(i, rows):
                    for y in range(j, cols):
                        if matrix[x, y] != 127:
                            found = False
                            break
                    if not found:
                        break
                    count += 1
                break
        if found:
            break
    return count