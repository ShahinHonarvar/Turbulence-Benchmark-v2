import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix.')
    if matrix.dtype.kind != 'i':
        raise ValueError('Matrix elements must be of integer type.')
    m, n = (matrix.shape[0], matrix.shape[1])
    count = 0
    for i in range(m):
        for j in range(n):
            for a in range(i, m):
                for b in range(j, n):
                    submatrix = matrix[i:a + 1, j:b + 1].flatten()
                    if len(set(submatrix)) == 1 and submatrix[0] == 1:
                        count += 1
    return count