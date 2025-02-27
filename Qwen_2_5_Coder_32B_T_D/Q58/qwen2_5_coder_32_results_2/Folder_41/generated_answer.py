import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = matrix.shape[0]
    for i in range(n):
        for j in range(n):
            for x in range(i, n):
                for y in range(j, n):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.size == 73 and np.all(submatrix == 73):
                        count += 1
    return count