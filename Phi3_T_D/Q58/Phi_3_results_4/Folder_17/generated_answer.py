import numpy as np

def submatrix_with_n_numbers(mat):
    if not isinstance(mat, np.ndarray):
        raise ValueError('Input must be a numpy matrix')
    if mat.ndim != 2:
        raise ValueError('Matrix must be two-dimensional')
    if mat.shape[0] * mat.shape[1] < 166:
        return 0

    def count_submatrices(matrix, count):
        rows, cols = matrix.shape
        for subrow_size in range(1, rows - 15):
            for subcol_size in range(1, cols - 15):
                submatrix = matrix[subrow_size:-(16 - subrow_size), subcol_size:-(16 - subcol_size)]
                count[0] += (submatrix == 166).sum()
        return count
    count = [0]
    return count