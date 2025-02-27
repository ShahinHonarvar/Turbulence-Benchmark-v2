import numpy as np

def submatrix_with_n_numbers(matrix):
    count, size = (0, matrix.shape[0])
    for i in range(size):
        for j in range(size):
            if i + 5 < size and j + 5 < size:
                for k in range(i, i + 6):
                    for l in range(j, j + 6):
                        if np.all(matrix[i:i + 6, j:j + 6]):
                            count += 1
    return count