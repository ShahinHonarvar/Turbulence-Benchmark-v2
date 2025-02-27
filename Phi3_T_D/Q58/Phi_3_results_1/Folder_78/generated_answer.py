import numpy as np

def submatrix_with_n_numbers(matrix):
    if not isinstance(matrix, np.ndarray):
        matrix = np.array(matrix)
    if matrix.ndim != 2:
        raise ValueError('The input must be a 2D numpy matrix')
    shape = matrix.shape
    count = 0
    for a in range(shape[0]):
        for b in range(shape[1]):
            length = 0
            submatrix_count = 0
            for x in range(a, shape[0]):
                for y in range(b, shape[1]):
                    length += 1
                    if length == 91:
                        submatrix_count += 1
                        break
                if length == 91:
                    break
            count += submatrix_count
    return count