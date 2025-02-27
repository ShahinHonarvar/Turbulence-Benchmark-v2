import numpy as np

def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError('Input must be a numpy matrix.')

    def check_submatrix(sub_matrix):
        return np.sum(sub_matrix) == 1

    def find_submatrices(matrix):
        rows, cols = matrix.shape
        for sr in range(rows):
            for sc in range(cols):
                for er in range(sr, rows):
                    for ec in range(sc, cols):
                        yield matrix[sr:er + 1, sc:ec + 1]
    result = [sub_matrix.tolist() for sub_matrix in find_submatrices(matrix) if check_submatrix(sub_matrix)]
    return result